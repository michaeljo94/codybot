# -*- coding: utf-8 -*-


class CommandActionRegistry:
    """This class handles association of commands and Actions"""

    _instance = None
    """CommandActionRegistry: Singleton instance variable"""
    _registry_dict = {}
    """dict: internal registry for actions

    this dictionary associates commands with BaseActions
    """

    def __init__(self):
        """this class is a Singleton use .instance() instead.

        Raises:
            RuntimeError: if instantiated by __init__()
        """
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        """Creates an instance of CommandActionRegistry if none is already instantiated"""
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def get_action(self, command_name):
        """ queries the registry for an action

        Args:
            command_name: command to query for

        Returns:
            BaseAction: if the action is found else None
        """
        return self._registry_dict.get(command_name)

    def add_action(self, command_name: str, action_obj):
        """ands an action to the registry

        Notes:
            If the command_name already exits it will be overwritten

        Args:
            command_name: name of the command (behaves like a key)
            action_obj: Actual action to register
        """
        self._registry_dict.update({command_name: action_obj})

    async def get_commands(self):
        """generates a list of all registered commands

        Yields
            keys of registered actions
        """
        for command in self._registry_dict.values():
            yield command
