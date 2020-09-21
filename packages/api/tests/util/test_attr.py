# -*- coding: utf-8 -*-

from backend.util.attr import map_to_obj

from unittest.mock import Mock


def test_map_to_obj_returns_all_attributes():
    expected_obj = 'bar'
    fake_objs = list(map(Mock, range(2)))

    for obj in fake_objs:
        obj.foo = expected_obj

    objs, _ = map_to_obj('foo', fake_objs)
    assert objs == [expected_obj, expected_obj]


def test_map_to_obj_returns_all_objects_without_the_attr():
    fake_objs = list(map(Mock, range(2)))

    for obj in fake_objs:
        delattr(obj, 'foo')

    _, objs = map_to_obj('foo', fake_objs)
    assert objs == fake_objs
