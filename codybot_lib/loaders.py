from codybot_lib.bot_actions.simple_responses import HelloAction, HelpAction, TimeAction
from codybot_lib.bot_actions.api_responses import PussyAction, DogAction, XKCDAction


class ActionLoader:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    async def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            await cls.register_actions()
        return cls._instance

    @classmethod
    async def register_actions(cls):
        HelloAction()
        HelpAction()
        TimeAction()
        PussyAction()
        DogAction()
        XKCDAction()
