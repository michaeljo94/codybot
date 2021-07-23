# -*- coding: utf-8 -*-
from typing import Coroutine, Any

from discord import Message, Client

from core.actions.base import BaseAction
from core.parsers import CommandParser


class ParameterActionMixin(BaseAction):
    async def get_parameters(self, message: Message) -> Coroutine[Any, Any, dict]:
        return CommandParser.get_parameters(message)

    async def run(self, client: Client, *args, **kwargs):
        parameters = await self.get_parameters(message=kwargs.get("message"))
        return await super().run(client, *args, parameters=parameters, **kwargs)
