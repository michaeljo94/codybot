# -*- coding: utf-8 -*-
import logging


class ImproperlyConfigured(Exception):
    """Raised whenever a CONFIG_MODULE does not configure a needed Setting"""

    def with_traceback(self, tb):
        logging.exception(tb)
        return super().with_traceback(tb)


class CommandNotFoundError(AttributeError):
    pass
