# -*- coding: utf-8 -*-
from abc import abstractmethod
from typing import Optional

from core.logging import Logger
from core.registries import CommandActionRegistry


class BaseAction:
    command_name: str
    command_desc = "No Description"
    command_trigger: Optional[str] = None
    logger: Logger

    def __init__(self):
        self.command_name = self.__class__.__name__

        if not self.command_trigger:
            self.command_trigger = (
                f"!{self.__class__.__name__.lower().removesuffix('action')}"
            )
        self.registry = CommandActionRegistry.instance()
        self.registry.add_action(self.command_trigger, self)

    @abstractmethod
    async def run(self, client, *args, **kwargs):
        pass
