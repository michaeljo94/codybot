# -*- coding: utf-8 -*-
from discord import Client, Message

from core.actions.mixins import ParameterActionMixin
from core.decorators import log
from core.actions.base import BaseAction


class SimpleResponseAction(BaseAction):
    @log
    async def run(self, client: Client, *args, **kwargs):
        message: Message = kwargs.get("message")
        if not message:
            return

        await message.channel.send(self.get_response(client, *args, **kwargs))

    def get_response(self, client, *args, **kwargs):
        return "You have overwrite SimpleResponseAction.get_message()"


class ParameterResponseAction(ParameterActionMixin, SimpleResponseAction):  # noqa
    pass
