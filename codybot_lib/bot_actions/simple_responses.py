from datetime import datetime

from codybot_lib.actions import SimpleResponseAction


class HelloAction(SimpleResponseAction):
    command_desc = "Greets the user"

    def get_response(self, client, *args, **kwargs):
        message = kwargs.get("message")
        return f"Hello {message.author.nick}"


class HelpAction(SimpleResponseAction):
    command_desc = "Prints this message"

    def get_response(self, client, *args, **kwargs):
        commands = "Commands:"
        for command in client.broker.registry.get_commands():
            commands += f"\n - {command.command_trigger}:\t{command.command_desc}"
        return commands


class TimeAction(SimpleResponseAction):
    command_desc = "Prints time at bots location"

    def get_response(self, client, *args, **kwargs):
        now = datetime.now()
        return f"It is {now.hour}:{now.minute}:{now.second} - {now.day}.{now.month}.{now.year}"