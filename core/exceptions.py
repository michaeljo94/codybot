# -*- coding: utf-8 -*-
import logging


class ImproperlyConfigured(Exception):
    def with_traceback(self, tb):
        logging.exception(tb)
        return super().with_traceback(tb)


class CommandNotFoundError(AttributeError):
    pass
