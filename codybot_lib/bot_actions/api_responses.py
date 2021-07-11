from functools import lru_cache
from typing import List

import requests

from codybot_lib.actions import SimpleResponseAction, ParameterResponseAction
from discord import Message, Client

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


class FukAction(ParameterResponseAction):
    command_desc = "Fuk of every (use `!fuk help` for more information)"
    _url = "https://www.foaas.com/"

    def get_response(self, client, *args, **kwargs):
        super().get_response(client, *args, **kwargs)
        return "Ich habs ja überschrieben!"

    # def operations(self) -> List[dict]:
    #     operations = requests.get(f"{self._url}operations", headers={"ACCEPT": "application/json"}).json()
    #     for operation in operations:
    #         yield operation
    #
    # def operations_names(self):
    #     return (operation.name for operation in self.operations())
