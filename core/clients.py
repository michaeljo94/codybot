# -*- coding: utf-8 -*-
import os

from discord import Client

from .brokers import CommandBroker
from .exceptions import CommandNotFoundError
from .loaders import ActionLoader


class CodyClient(Client):
    def __init__(self, *, loop=None, **options):
        self.broker = CommandBroker.instance(self)
        self._env_guild = os.getenv("DISCORD_GUILD")
        super().__init__(loop=loop, **options)

    async def on_ready(self):
        await ActionLoader.instance()
        print("..done!")

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f"Willkommen {member.name}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.author.bot:
            return

        try:
            await self.broker.run(message)
        except CommandNotFoundError:
            pass
