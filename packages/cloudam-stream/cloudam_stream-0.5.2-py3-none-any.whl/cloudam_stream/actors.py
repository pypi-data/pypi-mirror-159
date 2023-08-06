from typing import TypeVar, Generic
from .ports import _InputPort, _OutputPort

T = TypeVar('T')


class _Args(object):
    pass


class _Actor(Generic[T], object):

    def __init__(self, name: str = None, actor_id: str = None):
        self.__name = name
        self.__id = actor_id
        self.__output_ports = []
        self.__input_ports = []
        self.__parameters = {}
        self.__parameter_overrides = {}
        self.args = _Args()

    def begin(self):
        pass

    def end(self):
        pass

    def emit(self, data: T):
        for port in self.__output_ports:
            port.emit(data)

    def set_input_ports(self, input_ports: list[_InputPort]):
        self.__input_ports = input_ports

    def get_input_ports(self):
        return self.__input_ports

    def set_output_ports(self, output_ports: list[_OutputPort]):
        self.__output_ports = output_ports

    def get_output_ports(self):
        return self.__output_ports

    def set_parameters(self, parameters: {}):
        self.__parameters = parameters

    def get_parameters(self):
        return self.__parameters

    def set_parameter_overrides(self, parameter_overrides: {}):
        self.__parameter_overrides = parameter_overrides

    def get_parameter_overrides(self):
        return self.__parameter_overrides


class ComputeActor(_Actor):
    """
    处理消息流
    """

    def process(self, data: T):
        pass


class ParallelComputeActor(ComputeActor):

    pass


class SinkActor(_Actor):
    """输出结果文件"""

    def write(self, data: T):
        pass


class SourceActor(_Actor):
    """生产消息流"""

    def produce(self):
        pass
