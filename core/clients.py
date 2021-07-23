# -*- coding: utf-8 -*-
import os

from discord import Client

from core.brokers import CommandBroker
from core.exceptions import CommandNotFoundError
from core.loaders import ActionLoader


class CodyClient(Client):
    broker: CommandBroker
    """broker: CommandBroker

   This broker hold the CommandBroker later to be used by on_message
    """
    _env_guild: str
    """the active guilds name"""

    async def on_ready(self):  # noqa
        """initializes the bots features if the framework has been loaded"""
        self.broker = CommandBroker.instance(self)
        self._env_guild = os.getenv("DISCORD_GUILD")
        await ActionLoader.instance()
        print("..done!")

    async def on_member_join(self, member):  # noqa
        """event called if new member joins the guild"""
        await member.create_dm()
        await member.dm_channel.send(f"Willkommen {member.name}")

    async def on_message(self, message):  # noqa
        """event called if a member sends a message"""
        if message.author == self.user:
            return
        if message.author.bot:
            return

        try:
            await self.broker.run(message)
        except CommandNotFoundError:
            pass
