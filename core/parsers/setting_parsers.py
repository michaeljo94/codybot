# -*- coding: utf-8 -*-
class SettingParser:
    @staticmethod
    async def split_class_from_module(reference: str) -> [str, str]:
        """splits class and module references into importable strings

        Args:
           reference(str): reference to be split [module, class]
        """
        module = ".".join(reference.split(".")[:-1])
        class_ = reference.split(".")[-1]
        return module, class_
