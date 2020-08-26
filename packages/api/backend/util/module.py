# -*- coding: utf-8 -*-


def get_relative_name(module: object) -> str:
    """
    Extract the relative name of a module. The relative is the last
    name in the module path.

    Eg.: backend.event.a_nice_module -> a_nice_module is the relative name.

    :param module: a valid module object
    """

    return module.__name__.split('.')[-1]
