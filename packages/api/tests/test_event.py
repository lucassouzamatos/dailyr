# -*- coding: utf-8 -*-

from dailyr.event import CALLBACK_REG_NAME, register_availables
from dailyr.exception.event import MissingEventFunctionError
import pytest

from unittest.mock import Mock


def test_register_availables_calls_function_with_args():
    fake_module = Mock()
    expected_arg = 'foo'

    register_availables(expected_arg, modules=[fake_module])

    fake_fn = getattr(fake_module, CALLBACK_REG_NAME)
    fake_fn.assert_called_once_with(expected_arg)


def test_register_availables_fails_when_module_has_the_missing_callback():
    fake_module = Mock()

    # we have to actually fake a real module
    fake_module.__name__ = 'baz'

    # unregister fake attribute/function/whatever
    delattr(fake_module, CALLBACK_REG_NAME)

    with pytest.raises(MissingEventFunctionError):
        register_availables('bar', modules=[fake_module])


def test_register_availables_get_the_relative_module_name_when_failed():
    fake_module = Mock()

    # value that will be parsed to get the relative module name
    fake_module.__name__ = 'baz.foo'

    # unregister fake attribute/function/whatever
    delattr(fake_module, CALLBACK_REG_NAME)

    with pytest.raises(MissingEventFunctionError, match=r'.* foo.*'):
        register_availables('bar', modules=[fake_module])
