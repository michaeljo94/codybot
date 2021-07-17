# -*- coding: utf-8 -*-
from importlib import import_module

from .exceptions import ImproperlyConfigured
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
        try:
            actions = settings.INSTALLED_ACTIONS
        except AttributeError as ex:
            raise ImproperlyConfigured(
                "INSTALLED_ACTIONS not defined in CONFIG_MODULE"
            ) from ex

        for action in actions:
            try:
                module = ".".join(action.split(".")[:-1])
                class_ = action.split(".")[-1]
            except TypeError as ex:
                raise ImproperlyConfigured("INSTALLED_ACTIONS -> list[str]") from ex
            except IndexError as ix:
                raise ImproperlyConfigured(
                    "No module but an action has"
                    " been defined in "
                    "config.INSTALLED_ACTIONS"
                ) from ix

            try:
                module = import_module(module)
                class_ = getattr(module, class_)
                class_()
            except ImportError as ix:
                raise ImproperlyConfigured(
                    f"Action not found in {module.__name__}"
                ) from ix
            except AttributeError():
                pass
