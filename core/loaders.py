# -*- coding: utf-8 -*-
from importlib import import_module
from typing import Optional

from core.exceptions import ImproperlyConfigured
from core.parsers import SettingParser
from core.settings import SettingBuilder


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
    async def _get_actions(cls) -> Optional[list[str]]:
        """ aggregates actions to be loaded by the ActionLoader

        Returns:
            list of strings containing module references to actions

        Raises:
            ImproperlyConfigured: if CONFIG_MODULE is not defined in the environment_vars
        """
        settings = await SettingBuilder.get_settings()
        try:
            actions = settings.INSTALLED_ACTIONS
        except AttributeError as ex:
            raise ImproperlyConfigured(
                "INSTALLED_ACTIONS not defined in CONFIG_MODULE"
            ) from ex
        return actions

    @classmethod
    async def _register_action(cls, module: str, class_: str) -> None:
        """imports action from reference and instantiates it

        Args:
            module(str): module to import Action class from
            class_(str): name of the Action class to import and instantiate

        Raises:
            ImproperlyConfigured: if the Action referenced is not found.
        """
        try:
            module = import_module(module)
            class_ = getattr(module, class_)
            class_()
        except ImportError as ix:
            raise ImproperlyConfigured(f"Action not found in {module.__name__}") from ix
        except AttributeError():
            pass

    @classmethod
    async def _process_action_reference(cls, action_reference: str) -> [str, str]:
        """splits action references into importable strings

        Args:
            action_reference(str): class reference to be split
        """
        try:
            module, class_ = await SettingParser.split_class_from_module(
                action_reference
            )
        except TypeError as ex:
            raise ImproperlyConfigured("INSTALLED_ACTIONS -> list[str]") from ex
        return module, class_

    @classmethod
    async def register_actions(cls):
        for action in await cls._get_actions():
            module, class_ = await cls._process_action_reference(action)
            await cls._register_action(module=module, class_=class_)
