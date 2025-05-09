import os
import yaml

class Config:
    _config = None

    @classmethod
    def load_config(cls, file_path: str):
        """加载配置文件"""
        if cls._config is None:
            with open(file_path, "r", encoding="utf-8") as f:
                cls._config = yaml.safe_load(f)
        return cls._config

    @classmethod
    def get(cls, key: str, default=None):
        """获取配置项"""
        keys = key.split(".")
        value = cls._config
        for k in keys:
            value = value.get(k, {})
        return value or default


# 在模块加载时自动加载配置
config:Config = None

def init_config(file_path: str = "app/config/config.yml"):
    """初始化配置"""
    global config
    if config is None:
        config = Config()
        config.load_config(file_path)
    return config

def get_config(key: str, default=None):
    """获取配置项"""
    global config
    if config is None:
        return default
    return config.get(key, default)