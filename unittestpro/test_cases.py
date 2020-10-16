#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-10-12 16:15
# 导入unittest


import unittest

class Search:
    def Searchfun(self):
        print("Search")
        return True
# 继承unittest.TestCase
class TestSearch(unittest.TestCase):

    #  类级别，整个类开始和结束执行各执行一次
    @classmethod
    def setUpClass(cls):
        print("setUpclass")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls):
        print("tearDownclass")

    # 每个测试用例的前后各执行一次
    # def setUp(self):
    #     # self.search = Search()
    #     print("setUp")
    #
    # def tearDown(self):
    #     print("tearDown")

    # 以test_开头
    def test_Search(self):
        # search = Search()
        assert True == self.search.Searchfun()
        print("test_Search")

    def test_Search1(self):
        # search = Search()
        print("test_Search111")

    def test_Search2(self):
        # search = Search()
        print("test_Search222")

class TestSearch1(unittest.TestCase):
    def test_Search1(self):
        print("判断相等")
        self.assertEqual(1,1,"判断相等")
    def test_Search2(self):
        print("判断不相等")
        self.assertNotEqual(1,2,"判断不相等")
    def test_Search3(self):
        print("判断大于")
        self.assertGreater(2,1,"判断大于")
# if __name__ == '__main__':
    # 方法一：执行当前文件所有的unittest测试用例，全部执行
    # unittest.main()
    # 方法二：加入容器中执行，执行指定的测试用例，将要执行的测试用例添加到测试套件中，批量执行测试方法
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch1("test_Search1"))
    # suite.addTest(TestSearch1("test_Search2"))
    # unittest.TextTestRunner().run(suite)
    # 方法三：执行某个测试类，将测试类添加到测试套件里，批量执行测试类
    #verbosity默认值为1，不限制完整结果，即单个用例成功输出’.’,失败输出’F’,错误输出’E’;verbosity=2将输出完整的信息，verbosity=2是指测试结果的输出的详细程度，有0-6级，具体代码实现可看Python27\Lib\unittest\runner.py源代码
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=1).run(suite)

