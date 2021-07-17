# -*- coding: utf-8 -*-
from importlib import import_module

from .settings import SettingBuilder


class ActionLoader:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    async def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            await cls.register_actions()
        return cls._instance

    @classmethod
    async def register_actions(cls):
        settings = await SettingBuilder.get_settings()
        for action in settings.INSTALLED_ACTIONS:
            module = ".".join(action.split(".")[:-1])
            class_ = action.split(".")[-1]

            module = import_module(module)
            class_ = getattr(module, class_)
            class_()
