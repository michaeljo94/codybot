# -*- coding: utf-8 -*-
from discord import Message

from .exceptions import CommandNotFoundError
from .parsers import CommandParser
from .registries import CommandActionRegistry


class CommandBroker:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls, client):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.registry = CommandActionRegistry.instance()
            cls.client = client
        return cls._instance

    async def run(self, message: Message):
        command = await CommandParser.get_parameters(message)
        action = self.registry.get_action(command_name=command.get("_command"))
        try:
            await action.run(client=self.client, message=message)
        except AttributeError as ax:
            raise CommandNotFoundError() from ax
