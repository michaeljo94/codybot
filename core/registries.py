# -*- coding: utf-8 -*-
from core.actions import BaseAction


class CommandActionRegistry:
    _instance = None
    _registry_dict = {}

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def get_action(self, command_name) -> BaseAction:
        return self._registry_dict.get(command_name)

    def add_action(self, command_name: str, action_obj: BaseAction):
        self._registry_dict.update({command_name: action_obj})

    def get_commands(self):
        return [command for command in self._registry_dict.values()]
