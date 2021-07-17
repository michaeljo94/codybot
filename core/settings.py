# -*- coding: utf-8 -*-
import os
from importlib import import_module
from typing import Any


from .exceptions import ImproperlyConfigured


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
            try:
                config_obj = import_module(os.environ.get("CONFIG_MODULE"))
            except ImportError:
                config_module = os.environ.get("CONFIG_MODULE")
                if config_module:
                    raise ImproperlyConfigured(
                        f'CONFIG_MODULE="{config_module}" not an appropriate module'
                    )
                raise ImproperlyConfigured("CONFIG_MODULE not found")

            cls._settings = Settings(config=config_obj.__dict__)
        return cls._instance

    @classmethod
    async def get_settings(cls):
        await cls.instance()
        return cls._settings
