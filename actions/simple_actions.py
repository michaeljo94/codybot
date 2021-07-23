# -*- coding: utf-8 -*-
from datetime import datetime

from core.actions.generic import SimpleResponseAction


class HelloAction(SimpleResponseAction):
    command_name = "HelloAction"
    command_desc = "Greats the user"
    command_trigger = "!hello"
    delete_after = 10.0

    def get_response(self, client, *args, **kwargs):
        message = kwargs.get("message")
        return f"Hello {message.author.nick}"


class HelpAction(SimpleResponseAction):
    command_name = "HelpAction"
    command_desc = "Prints this message"
    command_trigger = "!help"
    delete_after = 10.0

    def get_response(self, client, *args, **kwargs):
        commands = "Commands:"
        for command in client.broker.registry.get_commands():
            commands += f"\n - {command.command_trigger}:\t{command.command_desc}"
        return commands


class TimeAction(SimpleResponseAction):
    command_name = "TimeAction"
    command_desc = "Prints time at bots location"
    command_trigger = "!time"
    delete_after = 10.0

    def get_response(self, client, *args, **kwargs):
        now = datetime.now()
        return f"It is {now.hour}:{now.minute}:{now.second} - {now.day}.{now.month}.{now.year}"
