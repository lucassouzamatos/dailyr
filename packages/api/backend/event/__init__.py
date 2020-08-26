# -*- coding: utf-8 -*-

# from . import ()
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

    :param app: a :class:`eve.Eve` object
    :param modules: list of available modules
    """

    # keep track of modules without callback
    #
    # if any module had failed, we can not continue so instead of
    # failing early, we try them all and remember the ones who
    # failed to complain to the developer
    failed_modules = []

    for module in modules or get_availables():
        # decides whether module has the callback
        if hasattr(module, CALLBACK_REG_NAME):
            callback = getattr(module, CALLBACK_REG_NAME)
            callback(app)
        else:
            mod_name = module.__name__.split('.')[-1]

            # add the module name to the list
            failed_modules.append(mod_name)

    if failed_modules:
        raise MissingEventFunctionError(CALLBACK_REG_NAME, failed_modules)
