from codybot_lib.bot_actions.text_response_actions import HelloAction, HelpAction, TimeAction, PussyAction, DogAction, \
    XKCDAction


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
        # package_dir = Path(__file__).resolve().parent
        # for (_, module_name, _) in iter_modules([package_dir]):
        #     module = import_module(f"{__name__}.")
