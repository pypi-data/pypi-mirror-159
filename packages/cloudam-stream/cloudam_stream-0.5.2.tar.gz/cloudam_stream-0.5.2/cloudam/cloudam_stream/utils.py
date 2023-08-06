import os
from loguru import logger
from lz4 import frame
import base64
import json
import pickle
from hashlib import sha256
import hmac
import requests
from pathlib import Path
from .constants import RedisKey

project_id = str(os.getenv("project_id"))
env_ip = str(os.getenv("env_ip"))

class FlowStateUtils:

    def __init__(self, redis_client):
        self.redis_client = redis_client

    """
    查询某一actor的整体状态
    """
    def get_actor_final_state(self, actor_name: str):
        # 查询算子整体状态
        state = self.redis_client.hget(RedisKey.REDIS_KEY_FOR_ACTOR_FINAL_STATE.value, actor_name)
        if state:
            state = state.decode()
        logger.info('【core----get_pre_actors_state】actor_name:{},redis_key:{}------>state:{}', actor_name, RedisKey.REDIS_KEY_FOR_ACTOR_FINAL_STATE.value,
                    state)
        return state


class Base64Utils:

    """
    base64 编码
    """
    @staticmethod
    def encode(source, encoding='utf-8'):
        source_bytes = source.encode(encoding)
        base64_bytes = base64.b64encode(source_bytes)
        base64_string = base64_bytes.decode(encoding)
        base64_string = base64_string.replace('=', '_')
        return base64_string

    """
    base64 解码
    """
    @staticmethod
    def decode(source, encoding='utf-8'):
        source = source.replace('_', '=')
        base64_bytes = source.encode(encoding)
        string_bytes = base64.b64decode(base64_bytes)
        string = string_bytes.decode(encoding)
        return string


class DictUtils:

    """
    根据属性名查询属性值
    """
    @staticmethod
    def get_property_value(object_desc, property_name, default=None):
        property_value = default
        if type(object_desc) == str:
            object_desc = json.loads(object_desc)
        if type(object_desc) == dict:
            property_value = object_desc.get(property_name, default)
        return property_value


class SerializeUtils:
    """
    序列化
    """
    @staticmethod
    def encode(obj):
        return pickle.dumps(obj)

    """
    反序列化
    """
    @staticmethod
    def decode(obj):
        return pickle.loads(obj)

    """
    序列化、压缩
    """
    @staticmethod
    def encode_lz4(obj):
        msg = pickle.dumps(obj)
        return frame.compress(msg)

    """
    反序列化、解压
    """
    @staticmethod
    def decode_lz4(obj):
        uncompress_obj = frame.decompress(obj)
        return pickle.loads(uncompress_obj)


class Sha256Utils:

    """
    拼装data
    """
    @staticmethod
    def data_str(**data: str):
        res = ""
        for key, value in data.items():
            res = res + key + "=" + value + "&"
        return res[:-1]

    """
    sha256加密
    """
    @staticmethod
    def hmac_sha256(data: str):
        secret_key = "fu@#4545dsfue734dhecj00fhf2rhdhwDHFfdjsddfD"
        if not secret_key:
            return None
        key_enc = secret_key.encode()
        data_enc = data.encode()
        data_enc = base64.b64encode(data_enc)
        print(data_enc)
        return base64.b64encode(hmac.new(key_enc, data_enc, digestmod=sha256).digest()).decode()


class BusinessUtils:

    @staticmethod
    def dataset_path(dataset_name: str, relative_path: str):
        parent = str(Path(relative_path).parent.as_posix())
        if parent == ".":
            parent = ""
        if parent == "":
            # 项目路径
            dataset_path = "/project/" + project_id + "/.dataset/" + dataset_name + "/"
            # 实际写入挂载路径
            write_path = "/ProjectData/.dataset/" + dataset_name + "/"
        else:
            dataset_path = "/project/" + project_id + "/" + parent + "/.dataset/" + dataset_name + "/"
            # 实际写入挂载路径
            write_path = "/ProjectData/" + parent + "/.dataset/" + dataset_name + "/"
        return dataset_path, write_path


class HttpRequestUtils:

    @staticmethod
    def insert_dataset(path: str, name: str, size: int):
        url = env_ip + "/cpp/data/insert"
        data = Sha256Utils.data_str(projectId=project_id, path=path, name=name)
        sign = Sha256Utils.hmac_sha256(data)
        body = {
            "projectId": project_id,
            "path": path,
            "name": name,
            "size": size,
            "token": sign
        }
        headers = {"Content-Type": "application/json"}
        res = requests.post(url, json=body, headers=headers)
        print("dataset insert res:" + res.text)