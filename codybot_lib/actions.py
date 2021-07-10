from codybot_lib.decoratros import log
from codybot_lib.registries import CommandActionRegistry
from discord import Message, Client


class BaseAction:
    command_name = "BaseAction"
    command_desc = "No Description"
    command_trigger = "!baseAction"

    def __init__(self):
        self.registry = CommandActionRegistry.instance()
        self.registry.add_action(self.command_trigger, self)

    async def run(self, client, *args, **kwargs):
        raise NotImplemented


class AnswerAction(BaseAction):
    command_name = "AnswerAction"
    command_trigger = "!answerAction"

    @log
    async def run(self, client: Client, *args, **kwargs):
        message: Message = kwargs.get("message")
        if not message: return
        if message.author == client.user: return

        if message.content == self.command_trigger:
            await message.channel.send(self.get_message(client, *args, **kwargs))

    def get_message(self, client, *args, **kwargs):
        return "You have overwrite AnswerAction.get_message()"
