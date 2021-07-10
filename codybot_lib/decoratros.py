from inspect import getclasstree

from discord import Message


def log(func):
    async def inner(*args, **kwargs):
        message: Message = kwargs.get("message")

        if message:
            time = message.created_at
            print(
                f"[{time.hour}:{time.minute}:{time.second}:{time.microsecond} - {time.day}-{time.month}:{time.year}] {message.author}: {message.content}")
        cache = await func(*args, **kwargs)
        if cache:
            print(cache)
        return cache

    return inner
