from codybot_lib.decoratros import log
from codybot_lib.registries import CommandActionRegistry
from discord import Message, Client


class BaseAction:
    command_name: str
    command_desc = "No Description"
    command_trigger: str

    def __init__(self):
        self.command_name = self.__class__.__name__
        self.command_trigger = f"!{self.__class__.__name__.lower().removesuffix('action')}"
        self.registry = CommandActionRegistry.instance()
        self.registry.add_action(self.command_trigger, self)

    @log
    async def run(self, client, *args, **kwargs):
        raise NotImplemented


class SimpleResponseAction(BaseAction):
    async def run(self, client: Client, *args, **kwargs):
        message: Message = kwargs.get("message")
        if not message: return
        if message.author == client.user: return

        if message.content == self.command_trigger:
            await message.channel.send(self.get_response(client, *args, **kwargs))

    def get_response(self, client, *args, **kwargs):
        return "You have overwrite SimpleResponseAction.get_message()"
