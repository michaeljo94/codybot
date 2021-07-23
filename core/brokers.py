# -*- coding: utf-8 -*-
from discord import Message

from core.actions.base import BaseAction
from core.exceptions import CommandNotFoundError
from core.parsers import CommandParser
from core.registries import CommandActionRegistry


class CommandBroker:
    _instance = None

    @classmethod
    def instance(cls, client):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.registry = CommandActionRegistry.instance()
            cls.client = client
        return cls._instance

    async def _get_action(self, message: Message) -> BaseAction:
        command = await CommandParser.get_parameters(message)
        return self.registry.get_action(command_name=command.get("_command"))

    async def _run_action(self, action: BaseAction, message: Message):
        try:
            await action.run(client=self.client, message=message)
        except AttributeError as ax:
            raise CommandNotFoundError() from ax

    async def run(self, message: Message):
        action = await self._get_action(message)
        await self._run_action(action, message)

    def __init__(self):
        raise RuntimeError("Call instance() instead")
