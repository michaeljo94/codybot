# -*- coding: utf-8 -*-
import os
from copy import deepcopy
from importlib import import_module
from typing import Any

from .exceptions import ImproperlyConfigured


class Settings:
    def __init__(self, config):
        if not config:
            config = {}
        config = config.__dict__

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
    async def _import_config(cls) -> object:
        """imports the config from env:CONFIG_MODULE

        Raises:
            ImproperlyConfigured: if no CONFIG_MODULE is specified
        """
        try:
            config_obj = import_module(os.environ.get("CONFIG_MODULE"))
        except ImportError as ie:
            config_module = os.environ.get("CONFIG_MODULE")
            if config_module:
                raise ImproperlyConfigured(
                    f'CONFIG_MODULE="{config_module}" not an appropriate module'
                )
            raise ImproperlyConfigured("CONFIG_MODULE not found") from ie
        return config_obj

    @classmethod
    async def instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        if not cls._settings:
            cls._settings = Settings(config=await cls._import_config())
        return cls._instance

    @classmethod
    async def get_settings(cls):
        _ = await cls.instance()
        return deepcopy(cls._settings)
