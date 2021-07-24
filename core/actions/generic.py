# -*- coding: utf-8 -*-
from typing import Optional

from discord import Client, Message

from core.actions.base import BaseAction
from core.actions.mixins import ParameterActionMixin
from core.decorators import log


class SimpleResponseAction(BaseAction):
    delete_after: Optional[float] = None

    @log
    async def run(self, client: Client, *args, **kwargs):
        message: Message = kwargs.get("message")
        if not message:
            return

        await message.channel.send(
            await self.get_response(client, *args, **kwargs),
            delete_after=self.delete_after,
        )

    async def get_response(self, client, *args, **kwargs):
        return "You have overwrite SimpleResponseAction.get_message()"


class ParameterResponseAction(ParameterActionMixin, SimpleResponseAction):  # noqa
    pass
