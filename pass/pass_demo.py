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

class Pass_Demo:

    def test(self):
        for letter in 'Python':
            if letter == 'h':
                pass
                print('这是 pass 块')
            print('当前字母 :', letter)
        print("Good bye!")


if __name__ == '__main__':
    Pass_Demo().test()