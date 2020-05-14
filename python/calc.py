#!/usr/bin/python用于指明解释器的路径，有时候可能需要用到（这是我mac系统中自带python的路径，视自己的情况而定）
#-*- coding:utf-8 -*-即用于解决中文编码问题，设置默认字符编码为utf-8
# @Author :xiaopingzi       表示作者名字
# @Time : 2020-05-11 11:17 用于显示当前时间

# type hints 类型提示


class Calc:
    def add(self, a:float, b:float):
        result = a+b
        return round(result,1)

    def div(self, a:float, b:float):
        result = a / b
        return round(result,1)

    def sub(self, a, b):
        result = a - b
        return round(result, 2)

    def mult(self, a, b):
        result = a * b
        return round(result,2)
