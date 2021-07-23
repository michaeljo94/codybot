# -*- coding: utf-8 -*-
from discord import Message, Client

from core.actions.base import BaseAction
from core.exceptions import CommandNotFoundError
from core.parsers import CommandParser
from core.registries import CommandActionRegistry


class CommandBroker:
    _instance = None

    @classmethod
    def instance(cls, client):
        """instanciates the CommandBroker hence its a Singleton

        Args:
            client(Client): discord client

        Returns:
            an instance of CommandBroker
        """
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.registry = CommandActionRegistry.instance()
            cls.client = client
        return cls._instance

    async def _get_action(self, message: Message) -> BaseAction:
        """queries an action designated by the given message

        Args:
            message(Message): message to parse for an action

        Returns:
            an instance of the action the message designates
        """
        command = await CommandParser.get_parameters(message)
        return self.registry.get_action(command_name=command.get("_command"))

    async def _run_action(self, action: BaseAction, message: Message):
        """executes an action given while passing the message

        Args:
            action: action to be executed
            message: message object to be given to the action
        """
        try:
            await action.run(client=self.client, message=message)
        except AttributeError as ax:
            raise CommandNotFoundError() from ax

    async def run(self, message: Message):
        """validates the message for an action and runs

        Args:
            message(Message): message to be validated
        """
        action = await self._get_action(message)
        await self._run_action(action, message)

    def __init__(self):
        """This Class is a Singleton.

        PLEASE USE .instance() INSTEAD!
        """
        raise RuntimeError("Call instance() instead")
