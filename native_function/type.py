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

class Type:

    def test(self):
        #一个参数实例
        print(type(1))
        print(type('runoob'))
        print(type([2]))
        print(type({0:'zero'}))
        x = 1
        print(type( x ) == int)

        # 三个参数
        X = type('X', (object,), dict(a=1))
        print(X)

class X(object):
    a = 1


if __name__ == '__main__':
    Type().test()