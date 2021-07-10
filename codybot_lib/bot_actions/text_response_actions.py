from datetime import datetime

import requests
import requests as rq
from discord import Message, TextChannel

from codybot_lib.actions import AnswerAction


class HelloAction(AnswerAction):
    command_name = "HelloAction"
    command_desc = "Greats the user"
    command_trigger = "!hello"

    def get_message(self, client, *args, **kwargs):
        message = kwargs.get("message")
        return f"Hello {message.author.nick}"


class HelpAction(AnswerAction):
    command_name = "HelpAction"
    command_desc = "Prints this message"
    command_trigger = "!help"

    def get_message(self, client, *args, **kwargs):
        commands = "Commands:"
        for command in client.broker.registry.get_commands():
            commands += f"\n - {command.command_trigger}:\t{command.command_desc}"
        return commands


class TimeAction(AnswerAction):
    command_name = "TimeAction"
    command_desc = "Prints time at bots location"
    command_trigger = "!time"

    def get_message(self, client, *args, **kwargs):
        now = datetime.now()
        return f"It is {now.hour}:{now.minute}:{now.second} - {now.day}.{now.month}.{now.year}"


class PussyAction(AnswerAction):
    command_name = "PussyAction"
    command_desc = "Generates a random cat file"
    command_trigger = "!pussy"

    def get_message(self, client, *args, **kwargs):
        return requests.get("https://aws.random.cat/meow").json().get("file")


class DogAction(AnswerAction):
    command_name = "DogAction"
    command_desc = "Generates a random dog file"
    command_trigger = "!woof"

    def get_message(self, client, *args, **kwargs):
        return requests.get("https://random.dog/woof.json").json().get("url")


class XKCDAction(AnswerAction):
    command_name = "XKCDAction"
    command_desc = "Displays latest XKCD"
    command_trigger = "!xkcd"

    def get_message(self, client, *args, **kwargs):
        url = "https://xkcd.com/info.0.json"
        data = requests.get(url).json()

        return f"#{data.get('num')}: {data.get('title')} D:{data.get('day')}\n {data.get('img')}"
