from discord import Message, Client

from codybot_lib.decoratros import log
from codybot_lib.registries import CommandActionRegistry


class BaseAction:
    command_name: str
    command_desc = "No Description"
    command_trigger: str

    def __init__(self):
        self.command_name = self.__class__.__name__
        self.command_trigger = (
            f"!{self.__class__.__name__.lower().removesuffix('action')}"
        )
        self.registry = CommandActionRegistry.instance()
        self.registry.add_action(self.command_trigger, self)

    @log
    async def run(self, client, *args, **kwargs):
        raise NotImplemented


class SimpleResponseAction(BaseAction):
    async def run(self, client: Client, *args, **kwargs):
        message: Message = kwargs.get("message")
        if not message:
            return
        if message.author == client.user:
            return

        await message.channel.send(self.get_response(client, *args, **kwargs))

    def get_response(self, client, *args, **kwargs):
        return "You have overwrite SimpleResponseAction.get_message()"


class ParameterActionMixin:
    async def get_parameters(self, message: Message) -> dict:
        rv_parameters: dict = {}
        split_message: list[str] = message.content.split(" ")
        parameterized_message: list[str] = split_message[1:]
        try:
            for parameter in parameterized_message:
                split_parameter = parameter.split(":", maxsplit=1)
                try:
                    rv_parameters.update({split_parameter[0]: split_parameter[1]})
                except IndexError:
                    rv_parameters.update({split_parameter[0]: None})
        except IndexError:
            return rv_parameters
        finally:
            return rv_parameters

    async def run(self, client: Client, *args, **kwargs):
        parameters = await self.get_parameters(message=kwargs.get("message"))
        return await super().run(client, *args, parameters=parameters, **kwargs)


class ParameterResponseAction(ParameterActionMixin, SimpleResponseAction):
    pass
