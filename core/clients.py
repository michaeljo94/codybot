# -*- coding: utf-8 -*-
import os

from discord import Client, Guild

from .brokers import CommandBroker
from .loaders import ActionLoader


class CodyClient(Client):
    def __init__(self, *, loop=None, **options):
        self.broker = CommandBroker.instance(self)
        self._env_guild = os.getenv("DISCORD_GUILD")
        super().__init__(loop=loop, **options)

    @property
    async def get_guild_by_name(self) -> Guild:
        guilds = self.guilds
        for guild in guilds:
            if guild.name == self._env_guild:
                return guild

    def draw_beep(self, guild_name="NoGuild", guild_id=-1):
        print(
            f"{self.user} has connected to Discord",
            f"{guild_name} (id: {guild_id})",
            end="\n",
        )

    async def on_ready(self):
        guild = await self.get_guild_by_name
        if guild:
            self.draw_beep(guild.name, guild.id)
        await ActionLoader.instance()

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f"Willkommen {member.name}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.broker.run(message)
