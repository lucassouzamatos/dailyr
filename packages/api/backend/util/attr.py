# -*- coding: utf-8 -*-

from typing import Tuple


def map_to_obj(name: str, objects: list) -> Tuple[list, list]:
    """
    From a list of objects, map each of them who contains a given
    attribute by name.

    The first item in the returned tuple is a list of attributes
    obtained from the objects. And the second item is a list of
    objects which does not contain the attribute.

    :param name: attribute name to find
    :param objects: the list of objects
    """

    succeededs, faileds = [], []

    for item in objects:
        # decides whether module has the callback
        if hasattr(item, name):
            succeededs.append(getattr(item, name))
        else:
            # add the module name to the list
            faileds.append(item)

    return succeededs, faileds
