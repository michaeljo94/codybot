# -*- coding: utf-8 -*-

import requests

from core.actions.generic import SimpleResponseAction


class PussyAction(SimpleResponseAction):
    command_name = "PussyAction"
    command_desc = "Generates a random cat file"
    command_trigger = "!pussy"

    async def get_response(self, client, *args, **kwargs):
        response = requests.get("https://aws.random.cat/meow")
        file = response.json().get("file") if response.status_code == 200 else None
        alt_text = "no pussy for you sir!"
        return file if file else alt_text


class DogAction(SimpleResponseAction):
    command_name = "DogAction"
    command_desc = "Generates a random dog file"
    command_trigger = "!woof"

    async def get_response(self, client, *args, **kwargs):
        return requests.get("https://random.dog/woof.json").json().get("url")


class XKCDAction(SimpleResponseAction):
    command_name = "XKCDAction"
    command_desc = "Displays latest XKCD"
    command_trigger = "!xkcd"

    async def get_response(self, client, *args, **kwargs):
        url = "https://xkcd.com/info.0.json"
        data = requests.get(url).json()

        return f"#{data.get('num')}: {data.get('title')} D:{data.get('day')}\n {data.get('img')}"


class DadJokeAction(SimpleResponseAction):
    command_name = "DadJokeAction"
    command_desc = "Displays a Dad Joke"
    command_trigger = "!dad"

    async def get_response(self, client, *args, **kwargs):
        url = "https://icanhazdadjoke.com/"
        data = requests.get(url, headers={"ACCEPT": "application/json"})
        if data.status_code != 200:
            return "Dad is not here at the moment."
        return data.json().get("joke")
