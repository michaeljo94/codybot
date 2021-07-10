from collections import Iterable

from discord import Message

from codybot_lib.registries import CommandActionRegistry


class CommandBroker:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls, client):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.registry = CommandActionRegistry.instance()
            cls.client = client
        return cls._instance

    async def run(self, message: Message):
        command_key = self.get_command(message.content)
        action = self.registry.get_action(command_name=command_key)
        if action:
            await action.run(client=self.client, message=message)

    def split_message(self, message: str):
        msg = message.lower().strip().split(" ")
        if type(msg) is str:
            msg = [msg, ]
        return msg

    def get_command(self, message: str):
        splits = self.split_message(message)
        if type(splits) == list and splits[0]:
            if splits[0][0] and splits[0][0] == "!":
                return splits[0]
        elif type(splits) == str and splits[0] == "!":
            return splits

    def get_usernames(self, message):
        splits = self.split_message(message)
        rv_usernames: list[str] = list()
        if self.get_command(splits):
            for split in splits[1:]:
                if split.lower()[0] == "@":
                    rv_usernames.append(split)
                else:
                    break
        return rv_usernames
