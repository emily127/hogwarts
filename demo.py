#!/usr/bin/python用于指明解释器的路径，有时候可能需要用到（这是我mac系统中自带python的路径，视自己的情况而定）
#-*- coding:utf-8 -*-即用于解决中文编码问题，设置默认字符编码为utf-8
# @Author : xaiopingzi  表示作者名字
# @Time : 2020-05-10 10:02 用于显示当前时间



from testing import demo2
from python import demo1

from python.demo1 import Demo1
from testing.demo2 import Demo2
from python.demo1 import *
from testing import *




# #实例化demo1
# Demo1()
# Demo2()
#
#
# print(demo1.hello)
# demo1.f()
#
#
# print(hello)
# f()

if __name__ == "__main__":
    print('a')