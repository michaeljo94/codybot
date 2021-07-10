import requests

from codybot_lib.actions import SimpleResponseAction


class PussyAction(SimpleResponseAction):
    command_name = "PussyAction"
    command_desc = "Generates a random cat file"
    command_trigger = "!pussy"

    def get_response(self, client, *args, **kwargs):
        return requests.get("https://aws.random.cat/meow").json().get("file")


class DogAction(SimpleResponseAction):
    command_name = "DogAction"
    command_desc = "Generates a random dog file"
    command_trigger = "!woof"

    def get_response(self, client, *args, **kwargs):
        return requests.get("https://random.dog/woof.json").json().get("url")


class XKCDAction(SimpleResponseAction):
    command_name = "XKCDAction"
    command_desc = "Displays latest XKCD"
    command_trigger = "!xkcd"

    def get_response(self, client, *args, **kwargs):
        url = "https://xkcd.com/info.0.json"
        data = requests.get(url).json()

        return f"#{data.get('num')}: {data.get('title')} D:{data.get('day')}\n {data.get('img')}"
