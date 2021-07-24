# -*- coding: utf-8 -*-
from datetime import datetime

from discord import Client, Message

from core.actions.generic import SimpleResponseAction


class GithubAction(SimpleResponseAction):
    command_name = "GithubAction"
    command_desc = "Cody on Github.com"
    command_trigger = "!github"

    async def get_response(self, client, *args, **kwargs):
        return "https://github.com/michaeljo94/codybot"


class HelloAction(SimpleResponseAction):
    command_name = "HelloAction"
    command_desc = "Greats the user"
    command_trigger = "!hello"
    delete_after = 10.0

    async def get_response(self, client, *args, **kwargs):
        message = kwargs.get("message")
        return f"Hello {message.author.nick}"


class HelpAction(SimpleResponseAction):
    command_name = "HelpAction"
    command_desc = "Prints this message"
    command_trigger = "!help"
    delete_after = 60.0

    async def get_response(self, client, *args, **kwargs):
        commands = "Commands:"

        async for command in self.registry.get_commands():
            commands += f"\n - {command.command_trigger}:\t{command.command_desc}"
        return commands

    async def run(self, client: Client, *args, **kwargs):
        await super().run(client, *args, **kwargs)
        message: Message = kwargs.get("message")
        if message:
            await message.delete()


class TimeAction(SimpleResponseAction):
    command_name = "TimeAction"
    command_desc = "Prints time at bots location"
    command_trigger = "!time"
    delete_after = 10.0

    async def get_response(self, client, *args, **kwargs):
        now = datetime.now()
        return f"It is {now.hour}:{now.minute}:{now.second} - {now.day}.{now.month}.{now.year}"
