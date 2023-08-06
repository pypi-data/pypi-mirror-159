from enum import Enum


class ActorState(Enum):
    # ----未知状态----
    UNKNOW: str = "UNKNOW"
    # ----算子的状态----
    # flow manager解析完工作流，遍历各算子并提交slurm前设置该算子状态为queued-->flow_processor.process_actors()
    QUEUED: str = "QUEUED"
    # slurm申请到节点，但还没开始消费时，状态为READY-->actor_wrapper.if __name__ == '__main__'
    READY: str = "READY"
    # 开始消费后状态为RUNNING-->actor_wrapper.process_source_actor()和actor_wrapper.loop_input_port()
    RUNNING: str = "RUNNING"
    # (定时任务)根据slurm的scontrol命令来判断timer.update_actor_state()
    SUCCESS: str = "SUCCESS"
    FAILED: str = "FAILED"
    CANCELLED: str = "CANCELLED"
    STOPPABLE: str = "STOPPABLE"


class RedisKey(Enum):
    # redis key
    # 算子间的关系
    REDIS_KEY_FOR_ACTOR_RELATION: str = 'flow_manager_for_actor_relation'
    # 算子的状态
    REDIS_KEY_FOR_ACTOR_STATE: str = 'flow_manager_for_actor_state'
    # 算子的整体状态
    REDIS_KEY_FOR_ACTOR_FINAL_STATE: str = 'flow_manager_for_actor_final_state'


class Types(Enum):
    String = str
    Int = int
    Float = float
    Bool = bool
    List = list
    Dict = dict


class MetaTypes(Enum):
    String = 1
    Pairs = 2
