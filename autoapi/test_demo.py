#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-08-11 10:03
import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth
class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.text)
        print(r.json())
        print(r.status_code)
        assert r.status_code == 200
    def test_query(self):
        payload = {
            "level": 1,
            "name": "megranet"
        }
        r1 = requests.get('http://httpbin.testing-studio.com/get',params=payload)
        print(r1.text)
        assert r1.status_code ==200
    #post方法，form表单提交
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "megranet"
        }
        r2 = requests.post('http://httpbin.testing-studio.com/post', data=payload)
        print(r2.text)
        assert r2.status_code == 200

    # def test_header(self):
    #     r3 = requests.get('http://httpbin.testing-studio.com/get', headers={"h": "header"})
    #     print(r3.text)
    #     print(r3.json())
    #     assert r3.status_code == 200
    #     assert r3.json()['headers']["H"] == "header"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "megranet"
        }
        r2 = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r2.text)
        assert r2.status_code == 200
    def test_hogwarts(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        print(r.json())
        print(r.status_code)
        # assert r.status_code == 200
        # assert r.json()['category_list']['categories'][0]['name'] == '社区治理'
        # #jsonpath格式的断言
        # assert jsonpath(r.json(),'$..name')[0] == '社区治理'
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to('社区治理'))

    def test_demo(self):
        url = 'http://httpbin.testing-studio.com/#/Cookies'
        #使用headers传递cookie
        # header = {"Cookie":"hogwarts"}
        #使用cookies传递cookie
        header = {"User-Agent":"hogwarts"}
        cookie_data = {"school":"hogwarts","class":"1"}
        r = requests.get(url=url,headers=header,cookies=cookie_data)
        print(r.request.headers)
    def test_auth(self):
        url = "http://httpbin.testing-studio.com/basic-auth/banana/123"
        r = requests.get(url=url,auth=HTTPBasicAuth("banana","123"))
        print(r.text)