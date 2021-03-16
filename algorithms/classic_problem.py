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
# V0.1      2021/3/15     First version                                 Zhang Lu
# ------------------------------------------------------------------------------

class ClassicProblem:

    # 将字符串列表['aycc', 'kh', 'llc', 'u', 'l'], 通过算法处理为['y', 'k', 'c', 'u', 'l'],
    # 对调首尾字符串的位置，拼接字符串列表中的字符，组成字符串‘LUCKY’
    def test1(self):

        lst = ['aycc', 'kh', 'llc', 'u', 'l']
        # 生成[-3,-2,-1,-1,-1]这样一个索引列表
        lst_inde = [2 - i if 2 - i < 0 else -1 for i in range(5, 0, -1)]
        print(lst_inde)
        # 将列表中每个字符串按索引列表中对应的索引位置取出来，组成新列表
        lst1 = list(map(lambda x, i: x[i], lst, lst_inde))
        # 列表翻转
        lst1.reverse()
        # 拼接成对应的字符串并转换为大写
        str = ''.join(lst1).upper()
        print(str)

    # 请写出以下程序的执行结果
    def test2(self):
        list_test = [{'day': 1, 'no': 101},
                     {'day': 2, 'no': 301},
                     {'day': 3, 'no': 3},
                     {'day': 1, 'no': 401},
                     {'day': 3, 'no': 201}
                     ]
        list_new = list(list_test)
        for m in list_test:
            if m['no'] <= 300:
                m['type'] = 'FB'
            else:
                m['type'] = 'BK'

        list_new[1]['day'] = 7
        list_new.pop()

        print(list_test)
        print(list_new)



if __name__ == '__main__':
    ClassicProblem().test2()
