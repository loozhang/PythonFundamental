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

def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a=hi()
print(a)
print(a())