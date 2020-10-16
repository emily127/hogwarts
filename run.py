#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-10-15 16:15

import unittest

from unittestpro.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    report_title = 'TestSearch用例执行报告'
    desc = 'TestSearch测试报告'
    report_file = '../unittestpro/testreport.html'
    testdir = '../unittestpro'
    discover = unittest.defaultTestLoader.discover(testdir,pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=1).run(discover)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
