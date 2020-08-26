# -*- coding: utf-8 -*-

from backend.util.module import (
    get_relative_name,
)

from unittest.mock import Mock


def test_get_relative_name_returns_last_name():
    fake_module = Mock()

    # value that will be parsed to get the relative module name
    fake_module.__name__ = 'bar.zii.baz.foo'

    result = get_relative_name(fake_module)
    assert result == 'foo'


def test_get_relative_name_when_path_is_already_relative():
    fake_module = Mock()

    # value that will be parsed to get the relative module name
    fake_module.__name__ = 'baz'

    result = get_relative_name(fake_module)
    assert result == 'baz'
