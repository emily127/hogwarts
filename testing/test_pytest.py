#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author :xiaopingzi
# @Time : 2020-05-11 16:52

import pytest







#任何以test_开头的方法都可以识别到
from python.calc import Calc



class TestCalc:
    # 加法，正数，0，负数，大数，小数，非法字符
    data = [[1,2,3], [0,0,0], [-1,-2,-3], [0.1,0.2,0.3], [0.1, 1, 1.1], [0.1, -1, -0.9], [1, 'a', ''], [1, '$', ''], [1, '', ''], [9999999, 9999999, 19999998]]
    @pytest.mark.parametrize('a,b,expect',data)
    def test_add(self,a,b,expect):
        self.calc = Calc()
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            result = self.calc.add(a,b)
            assert result == expect
        else:
            pytest.xfail(reason = 'type is error')
    #
    # # 除法 整数，除数为0，小数，负数,大数，非法字符
    data1 = [[2,1,2],[1,0,''],[0.2,0.1,2],[-2,-1,2],[9999999,1,9999999],[-2,1,-2],[1,'a',''],['$',2,''],['','',''],[0,1,0]]
    @pytest.mark.parametrize('a,b,expect',data1)
    def test_div(self,a,b,expect):
        self.calc = Calc()
        if b == 0:
            pytest.xfail(reason = 'divisor can\'t be zero')
        elif isinstance(a,(int,float)) and isinstance(b,(int,float)):
            result = self.calc.div(a,b)
            assert result == expect
        else:
            pytest.xfail(reason='type is error')
    # 乘法  正数，负数，小数，整数，0，大数,1，非法字符
    data2 = [[1,2,2],[1,1,1],[1,-3,-3],[0,1,0],[0.1,0.1,0.01],[9999999,9999999,99999980000001],[-2,-2,4],['',1,''],['a',2,''],['$',3,'']]
    @pytest.mark.parametrize('a,b,expect',data2)
    def test_mult(self,a,b,expect):
        self.calc = Calc()
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            result = self.calc.mult(a, b)
            assert result == expect
        else:
            pytest.xfail(reason='type is error')

    # 减法  正数，负数，小数，整数，0，大数,非法字符
    data3 = [[1,1,0],[0,5,-5],[-5,3,-8],[0.3,-0.1,0.4],[-0.2,0.1,-0.3],[9999999,34,9999965],[1,'',''],['a',2,''],['$',3,'']]
    @pytest.mark.parametrize('a,b,expect',data3)
    def test_sub(self,a,b,expect):
        self.calc = Calc()
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = self.calc.sub(a, b)
            assert result == expect
        else:
            pytest.xfail(reason='type is error')






 # pytest.main(['-vs','test_pytest.py::TestCalc::test_div'])
# if __name__ == '__main__':
#     pytest.main(['-vs','test_pytest.py::TestCalc::test_div'])