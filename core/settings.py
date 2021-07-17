# -*- coding: utf-8 -*-
import os
from importlib import import_module
from typing import Any


class Settings:
    def __init__(self, config):
        if not config:
            config = {}
        for key, val in config.items():
            if not key.startswith("__"):
                super.__setattr__(self, key, val)

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError(f"{self.__class__.__name__} is Immutable!")


class SettingBuilder:
    _instance = None
    _settings = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    async def instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        if not cls._settings:
            config_obj = import_module(os.environ.get("CONFIG_MODULE", "config"))
            cls._settings = Settings(config=config_obj.__dict__)
        return cls._instance

    @classmethod
    async def get_settings(cls):
        await cls.instance()

        return cls._settings
