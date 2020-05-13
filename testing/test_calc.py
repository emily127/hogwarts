#!/usr/bin/python用于指明解释器的路径，有时候可能需要用到（这是我mac系统中自带python的路径，视自己的情况而定）
#-*- coding:utf-8 -*-即用于解决中文编码问题，设置默认字符编码为utf-8
# @Author :xiaopingzi       表示作者名字
# @Time : 2020-05-11 11:21 用于显示当前时间


import sys

# print(sys.path)
#添加上一级路径
sys.path.append('..')
import unittest

from python.calc import Calc


class TestCal(unittest.TestCase):
    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1,2)
        print(result)
        self.assertEqual(3,result)

unittest.main()



