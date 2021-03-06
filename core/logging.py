# -*- coding: utf-8 -*-
import logging

from core.settings import SettingBuilder


class Logger:
    @staticmethod
    async def get_logger(logger_name):
        """creates logger designated by logger_name

        Args:
            logger_name: name of the logging scope

        Returns:
            logging.Logger
        """
        logger = logging.getLogger(logger_name)
        return await Logger._build_handlers(logger)

    @staticmethod
    async def _build_handlers(logger):
        """sets up a given logger

        Args:
            logger: logger to configure

        Returns:
            logging.Logger
        """
        settings = await SettingBuilder.get_settings()

        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(settings.LOG_FILE)
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(logging.ERROR)

        c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        f_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        return logger
