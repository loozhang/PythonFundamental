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
# V0.1      2021/3/10     First version                                 Zhang Lu
# ------------------------------------------------------------------------------
from array import array
from functools import reduce


class Practice:

    def test(self):
        g = lambda x:x+1
        print(g(1))
        foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
        print(list(filter(lambda x: x % 3 == 0, foo)))
        print(list(map(lambda x: x * 2 + 10, foo)))
        print(reduce(lambda x, y: x + y, foo))

if __name__ == '__main__':
    Practice().test()