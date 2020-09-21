# -*- coding: utf-8 -*-

from backend.util.format import msg_from_list


class MissingEventFunctionError(AttributeError):
    """
    Represents the error when some modules have a missing
    function to register the application events.
    """

    def __init__(self, fn_name: str, modules: list):
        error = f'Modules have a missing "{fn_name}" function:'
        super().__init__(msg_from_list(error, modules))
