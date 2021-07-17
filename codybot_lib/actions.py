# -*- coding: utf-8 -*-
from typing import Coroutine, Any

from discord import Message, Client

from codybot_lib.decoratros import log
from codybot_lib.parsers import CommandParser
from codybot_lib.registries import CommandActionRegistry


class BaseAction:
    command_name: str
    command_desc = "No Description"
    command_trigger: str

    def __init__(self):
        self.command_name = self.__class__.__name__
        self.command_trigger = (
            f"!{self.__class__.__name__.lower().removesuffix('action')}"
        )
        self.registry = CommandActionRegistry.instance()
        self.registry.add_action(self.command_trigger, self)

    @log
    async def run(self, client, *args, **kwargs):
        raise NotImplemented


class SimpleResponseAction(BaseAction):
    async def run(self, client: Client, *args, **kwargs):
        message: Message = kwargs.get("message")
        if not message:
            return

        await message.channel.send(self.get_response(client, *args, **kwargs))

    def get_response(self, client, *args, **kwargs):
        return "You have overwrite SimpleResponseAction.get_message()"


class ParameterActionMixin:
    async def get_parameters(self, message: Message) -> Coroutine[Any, Any, dict]:
        return CommandParser.get_parameters(message)

    async def run(self, client: Client, *args, **kwargs):
        parameters = await self.get_parameters(message=kwargs.get("message"))
        return await super().run(client, *args, parameters=parameters, **kwargs)


class ParameterResponseAction(ParameterActionMixin, SimpleResponseAction):
    pass
