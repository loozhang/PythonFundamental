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

class Function_Demo1:

    def hi(name="yasoob"):
        print("now you are inside the hi() function")

        def greet():
            return "now you are in the greet() function"

        def welcome():
            return "now you are in the welcome() function"

        print(greet())
        print(welcome())
        print("now you are back in the hi() function")

if __name__ == '__main__':
    Function_Demo1().greet()