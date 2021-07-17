# -*- coding: utf-8 -*-
from discord import Message


class CommandParser:
    """
    ParameterParser: Parses messages to be used like cli commands
    """

    @staticmethod
    async def is_command(parameter: str) -> bool:
        """
        is_command: checks whether the given parameter is formatted like a valid command
        :param parameter: parameter to be validated
        :return: True if formatted correctly else False
        """
        if parameter.lower().startswith("!"):
            return True
        return False

    @staticmethod
    async def get_parameters(message: Message) -> dict:
        """
        get_parameters: builds a dictionary with all detectable parameters
        :param message: Discord message
        :return: dictionary with _command and parameters
        """
        rv_parameters: dict = {}
        split_message: list[str] = message.content.split(" ")
        parameterized_message: list[str] = split_message[1:]

        try:
            # Checks for Command
            if await CommandParser.is_command(split_message[0]):
                rv_parameters.update({"_command": split_message[0]})

            # Parses and splits parameter list
            for parameter in parameterized_message:
                split_parameter = parameter.split(":", maxsplit=1)
                try:
                    rv_parameters.update({split_parameter[0]: split_parameter[1]})
                except IndexError:
                    rv_parameters.update({split_parameter[0]: None})

        except IndexError:
            return rv_parameters
        return rv_parameters
