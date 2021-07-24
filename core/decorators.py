# -*- coding: utf-8 -*-
from logging import Logger

from discord import Message

from core.logging import Logger


def log(func):
    """ logs a function with logging

    Args:
        func: function reference to log

    Returns:
        function output
    """

    async def inner(*args, **kwargs):
        message: Message = kwargs.get("message")
        logger: Logger = await Logger.get_logger(func.__name__)
        cache = await func(*args, **kwargs)
        logger.info(f"{message.author}:{message.content} -> {cache}")

        return cache

    return inner
