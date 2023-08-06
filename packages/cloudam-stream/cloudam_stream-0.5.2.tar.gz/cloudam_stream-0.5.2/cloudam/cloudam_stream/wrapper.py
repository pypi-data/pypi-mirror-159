import os
import importlib
import json
from nanoid import generate
from redis.client import StrictRedis
from redis.connection import ConnectionPool
from .actors import _Args, _Actor, ComputeActor, SinkActor, SourceActor, ParallelComputeActor
from .utils import FlowStateUtils, Base64Utils, DictUtils, SerializeUtils
from .constants import *
from .streams import RedisConsumer, RedisProducer
from .payload import Record
from .ports import JsonInputPort, RecordInputPort
from loguru import logger
import types

""" 
异步处理每个actor(除了SourceActor)的process，并实时判断actor是否应该结束，只处理一个port对应一个上游actor的情况
"""


class StreamApp(object):
    __parameters_dynamic_import = "cloudam_stream.parameters"
    __ports_dynamic_import = "cloudam_stream.ports"

    actor_id: str
    current_actor_state: str = ActorState.READY.value
    current_actor_name: str
    redis_client: StrictRedis
    flow_depth: int
    actor_level: int
    parallel_index: int
    state_manager: FlowStateUtils
    project_id: str

    def __init__(self, actor: _Actor):
        self.actor = actor

    def check_failed(self, upstream_actors):
        all_failed = True
        for upstream_actor in upstream_actors:
            upstream_actor_state = self.state_manager \
                .get_actor_final_state(upstream_actor)
            # 如果上游算子有至少一个没有结束，继续
            if not upstream_actor_state == ActorState.FAILED.value:
                all_failed = False
                break
        return all_failed

    def check_finished(self, upstream_actors):
        # 是否停止该actor
        finished = True
        for upstream_actor in upstream_actors:
            upstream_actor_state = self.state_manager \
                .get_actor_final_state(upstream_actor)
            # 如果上游算子有至少一个没有结束，继续
            if not (upstream_actor_state == ActorState.SUCCESS.value
                    or upstream_actor_state == ActorState.FAILED.value
                    or upstream_actor_state == ActorState.CANCELLED.value):
                finished = False
                break
        return finished

    def loop_input_port(self):
        if isinstance(self.actor, SourceActor):
            # 处理sourceActor
            for item in self.actor.produce():
                self.actor.emit(item)
        else:
            stream_names_input_map = {}
            upstream_actors = []
            for input_port in self.actor.get_input_ports():
                stream_names_input_map[input_port.channel] = input_port
                upstream_actors.append(input_port.upstream_actor_name)
            consumer_id = generate()
            group_name = self.current_actor_name
            while True:
                consumer = RedisConsumer(self.redis_client, group_name, stream_names_input_map.keys())
                msgs = consumer.consume(consumer_id, 1)
                # 如果消息为空，判断上游所有算子状态是否结束
                if len(msgs) <= 0:
                    if self.check_failed(upstream_actors):
                        raise Exception("all upstream job failed!")
                    if self.check_finished(upstream_actors):
                        break
                for msg in msgs:
                    # 解析stream_name
                    stream_name = msg[0].decode()
                    input_port = stream_names_input_map[stream_name]
                    msg_items = msg[1]
                    for msg_item in msg_items:
                        self.process_msg(msg_item, consumer, stream_name, input_port)

    """消息处理"""

    def process_msg(self, msg_item, consumer, stream_name, input_port):
        # 解析消息ID
        msg_id = msg_item[0]
        # 解析消息体
        msg_body = msg_item[1][b'']
        # 解析消息体json格式
        msg_object = SerializeUtils.decode(msg_body)
        # 确认消息消费完毕
        consumer.ack(stream_name, msg_id)
        # 获取消息payload
        content = msg_object.get_payload()
        if isinstance(self.actor, SinkActor):
            if isinstance(input_port, JsonInputPort):
                # 处理sink算子
                self.actor.write(data=content)
            else:
                raise Exception("only support jsonInputPort now")
        elif isinstance(self.actor, ComputeActor) or isinstance(self.actor, ParallelComputeActor):
            if isinstance(input_port, JsonInputPort):
                # 处理 compute 算子
                item = self.actor.process(data=content)
                self.actor.emit(item)
            else:
                raise Exception("only support jsonInputPort now")
        else:
            pass

    """
    处理SourceActor
    """

    def process_actor(self):
        self.actor.begin()
        self.loop_input_port()
        end_records = self.actor.end()
        if isinstance(end_records, types.GeneratorType):
            for record in end_records:
                self.actor.emit(record)

    """
    获取actor的input_port
    """

    def get_actor_input_ports(self, actor_desc: dict) -> list:
        input_ports_json = DictUtils.get_property_value(actor_desc, 'input_ports', [])
        input_ports = []
        for input_port_json in input_ports_json:
            # port的类型
            port_class_name = input_port_json.get('class')
            # port的名称
            port_name = input_port_json.get('name')
            # port依赖的上游actor
            connect = input_port_json['connect'][0]
            upstream_actor_name = connect['actor']
            upstream_output_port = connect['port']
            input_port_module = importlib.import_module(self.__ports_dynamic_import)
            port_class = getattr(input_port_module, port_class_name)
            input_port = port_class(actor_name=self.current_actor_name)
            input_port.connect(upstream_output_port=upstream_output_port, upstream_actor_name=upstream_actor_name)
            # 把用户定义的port空对象用真实的对象覆盖
            setattr(self.actor, port_name, input_port)
            input_ports.append(input_port)
        return input_ports

    """
    获取actor的output_port
    """

    def get_actor_output_ports(self, actor_desc: dict) -> list:
        output_ports_json = DictUtils.get_property_value(actor_desc, 'output_ports', [])
        output_ports = []
        producer = RedisProducer(redis_client=self.redis_client, flow_depth=self.flow_depth,
                                 actor_level=self.actor_level)
        for output_port_json in output_ports_json:
            # port的类型
            port_class_name = output_port_json.get('class')
            # port的名称
            port_name = output_port_json.get('name')
            # port依赖的上游actor
            output_port_module = importlib.import_module(self.__ports_dynamic_import)
            port_class = getattr(output_port_module, port_class_name)
            output_port = port_class(producer=producer, port_name=port_name, actor_name=self.current_actor_name)
            output_ports.append(output_port)
            # 把用户定义的port空对象用真实的对象覆盖
            setattr(self.actor, port_name, output_port)
        return output_ports

    """
    获取actor的params
    """

    def get_actor_params(self, actor_desc: dict) -> _Args:
        params_json = DictUtils.get_property_value(actor_desc, 'parameters', [])
        args = _Args()
        for param in params_json:
            # type
            param_type = param.get('type')
            # param的变量名
            param_variable = param.get('variable')
            # param显示的名称
            param_name = param.get('name')
            # param显示的值
            param_value = param.get('value')
            # param显示的描述
            # param_description = param.get('description')
            # port依赖的上游actor
            param_module = importlib.import_module(self.__parameters_dynamic_import)
            param_class = getattr(param_module, param_type)
            param = param_class(name=param_name)
            setattr(args, param_variable, param_value)
            setattr(args, param_variable + "_object", param)
        return args

    def run(self):
        self.actor_id = os.getenv("actor_id")
        self.flow_depth = int(os.getenv("flow_depth"))
        self.actor_level = int(os.getenv("actor_level"))
        self.parallel_index = int(os.getenv("parallel_index"))
        self.project_id = str(os.getenv("project_id"))

        redis_host = os.getenv("redis_host")
        pool = ConnectionPool(max_connections=1, host=redis_host, port=6379, password='123456')
        self.redis_client = StrictRedis(connection_pool=pool)
        self.state_manager = FlowStateUtils(self.redis_client)

        # 获取actor 描述
        actor_desc = os.getenv("actor_desc")
        # base64解码参数
        actor_desc_arg = Base64Utils.decode(actor_desc)
        actor_json = json.loads(actor_desc_arg)
        self.current_actor_name = actor_json.get('name')

        # set actor 变量参数
        params = self.get_actor_params(actor_json)
        logger.info("actor_json>>>>" + json.dumps(actor_json))
        logger.info("params>>>>" + str(params))
        self.actor.args = params
        # TODO get_set_param,get_set_runtime_param
        input_ports = self.get_actor_input_ports(actor_json)
        logger.info("input_ports>>>>" + str(input_ports))
        output_ports = self.get_actor_output_ports(actor_json)
        logger.info("output_ports>>>>" + str(output_ports))
        self.actor.set_input_ports(input_ports)
        self.actor.set_output_ports(output_ports)
        # 设置actor状态为已开始
        logger.info("process_actor>>>>>start")
        self.process_actor()
        logger.info("process_actor>>>>>end")
