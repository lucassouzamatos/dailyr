# -*- coding: utf-8 -*-

# from . import ()
from backend.util.attr import map_to_obj
from backend.util.module import get_relative_name
from backend.exception.event import MissingEventFunctionError
from eve import Eve


CALLBACK_REG_NAME = 'register'


def get_availables() -> list:
    """
    Specify the default available modules to be registered.
    """

    return []


def register_availables(app: Eve, modules: list = None) -> None:
    """
    Register all available events using callback functions. The eve
    object is passed as argument to the callback of available modules.

    It fails before executing the callbacks when any module does not have
    the required callback attribute.

    :param app: a :class:`eve.Eve` object
    :param modules: list of available modules
    """

    callbacks, failed_modules = map_to_obj(CALLBACK_REG_NAME,
                                           modules or get_availables())

    # before even executing the callbacks
    if failed_modules:
        module_names = map(get_relative_name, failed_modules)
        raise MissingEventFunctionError(CALLBACK_REG_NAME, module_names)

    # pass the execution to each callback
    for callback in callbacks:
        callback(app)
