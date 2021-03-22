# -*- coding=utf-8 -*-

"""
About this module

Description of classes

Description of methods

"""

__authors__ = [
    '"Zhang Lu" <zhanglu1982@outlook.com>',
]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2021/3/22     First version                                 Zhang Lu
# ------------------------------------------------------------------------------

from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return ("Function is running")


can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run