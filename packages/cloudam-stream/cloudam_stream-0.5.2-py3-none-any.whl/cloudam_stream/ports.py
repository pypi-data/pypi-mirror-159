from typing import TypeVar, Generic
from .payload import Message, Record
from .streams import RedisProducer
from .utils import SerializeUtils
import json
from loguru import logger


T = TypeVar("T")


class __Port:

    # 初始化数据，生成需要的相关配置
    def __init__(self, port_name: str = "", actor_name: str = ""):
        self.port_name = port_name
        self.actor_name = actor_name


class _InputPort(Generic[T], __Port):

    upstream_output_port: str = ""
    upstream_actor_name: str = ""
    channel: str = ""

    def __init__(self, actor_name: str = ""):
        self.actor_name = actor_name
        super(_InputPort, self).__init__("", actor_name)

    def connect(self, upstream_output_port: str = "", upstream_actor_name: str = ""):
        self.upstream_output_port = upstream_output_port
        self.upstream_actor_name = upstream_actor_name
        self.channel = upstream_actor_name.replace(' ', '_') + '&' + upstream_output_port.replace(' ', '_')


class BinaryInputPort(_InputPort[bytes]):

    pass


class TextInputPort(_InputPort[str]):

    pass


class FloatInputPort(_InputPort[float]):

    pass


class JsonInputPort(_InputPort[dict]):

    pass


class RecordInputPort(_InputPort[Record]):

    pass


class _OutputPort(Generic[T], __Port):

    index = 1

    def __init__(self, producer: RedisProducer = None, port_name: str = None, actor_name: str = None):
        if port_name and actor_name:
            self.channel = actor_name.replace(' ', '_') + '&' + port_name.replace(' ', '_')
        self.producer = producer
        super(_OutputPort, self).__init__(port_name, actor_name)

    def __convert_json__(self, data):
        meta = {"index": self.index}
        if isinstance(data, tuple):
            if isinstance(data[1], dict):
                meta.update(data[1])
            if len(data) > 2:
                content = {"record": data[0], "meta": meta, "log": data[2]}
            else:
                content = {"record": data[0], "meta": meta, "log": ""}
        else:
            content = {"record": data, "meta": meta, "log": ""}
        self.index += 1
        return content

    def emit(self, data: T):
        if isinstance(self, JsonOutputPort):
            self._emit(self.__convert_json__(data))
        else:
            raise Exception("only support JsonOutputPort now")

    def _emit(self, payload: T):
        message_object = Message(payload, "0", type(payload).__name__)
        logger.info(json.dumps(message_object.__dict__))
        encode_msg = SerializeUtils.encode(message_object)
        self.producer.produce(self.channel, encode_msg)


class TextOutputPort(_OutputPort[str]):

    pass


class BinaryOutputPort(_OutputPort[bytes]):

    pass


class IntOutputPort(_OutputPort[int]):

    pass


class FloatOutputPort(_OutputPort[float]):

    pass


class JsonOutputPort(_OutputPort[dict]):

    pass


class RecordOutputPort(_OutputPort[Record]):

    pass


