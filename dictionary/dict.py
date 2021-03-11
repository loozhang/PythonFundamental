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

class Dict:

    def test(self):
        dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
        print("字典值 : %s" % dict.items())

        # 遍历字典列表
        for key, values in dict.items():
            print(key, values)

if __name__ == '__main__':
    Dict().test()