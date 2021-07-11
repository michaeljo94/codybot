from functools import lru_cache
from typing import List

import requests

from codybot_lib.actions import SimpleResponseAction
from discord import Message

from codybot_lib.exeptions import TooFewArgumentsException


class PussyAction(SimpleResponseAction):
    command_desc = "Generates a random cat file"

    def get_response(self, client, *args, **kwargs):
        return requests.get("https://aws.random.cat/meow").json().get("file")


class DogAction(SimpleResponseAction):
    command_desc = "Generates a random dog file"

    def get_response(self, client, *args, **kwargs):
        return requests.get("https://random.dog/woof.json").json().get("url")


class XKCDAction(SimpleResponseAction):
    command_desc = "Displays latest XKCD"

    def get_response(self, client, *args, **kwargs):
        url = "https://xkcd.com/info.0.json"
        data = requests.get(url).json()

        return f"#{data.get('num')}: {data.get('title')} D:{data.get('day')}\n {data.get('img')}"


class DadJokeAction(SimpleResponseAction):
    command_desc = "Displays a Dad Joke"

    def get_response(self, client, *args, **kwargs):
        url = "https://icanhazdadjoke.com/"
        data = requests.get(url, headers={"ACCEPT": "application/json"})
        if data.status_code != 200:
            return "Dad is not here at the moment."
        return data.json().get("joke")


class FukAction(SimpleResponseAction):
    command_desc = "Fuk of every (use `!fuk help` for more information)"
    _url = "https://www.foaas.com/"

    # def operations(self) -> List[dict]:
    #     operations = requests.get(f"{self._url}operations", headers={"ACCEPT": "application/json"}).json()
    #     for operation in operations:
    #         yield operation
    #
    # def operations_names(self):
    #     return (operation.name for operation in self.operations())

    def _build_message_parts(self, message: Message):
        message_splits:List[str] = message.content.strip().split(" ")
        rv_dict = dict()
        try:
            for split in message_splits[2:]:
                if ":" in split:
                    arg, val = split.split(":")
                    rv_dict.update({arg: val})
        except IndexError as e:
            raise TooFewArgumentsException
        return rv_dict


    def get_response(self, client, *args, **kwargs):
        message: Message = kwargs.get("message")
        try:
            params = self._build_message_parts(message)
        except TooFewArgumentsException:
            params = dict()

        print(params)

        return ""
