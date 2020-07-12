#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-12 10:34 
import pytest

@pytest.fixture()
def fix():
    print("开始计算")
    yield
    print("计算结束")