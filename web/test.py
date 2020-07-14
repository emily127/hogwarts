#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-05-13 10:14

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup(self):
        #启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #隐式等待
        #self.driver.implicitly_wait(3)
    def teardown(self):
        #进行资源回收
        self.driver.quit()

    def test_hogwarts(self):
        #打开被测网址
        self.driver.get("https://ceshiren.com/")
        #直接等待
        # time.sleep(5)
        # print("hello")
        self.driver.find_element_by_xpath('//*[@title="所有分类"]').click()
        # time.sleep(5)

        # def wait(x):
        #     return len(self.driver.find_elements_by_xpath("//*[@class='default']")) == 1
        # WebDriverWait(self.driver,10).until(wait)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class='default']")))
        print("selenium")
        self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()

#
# def test_selenium():
#     browser = webdriver.Chrome()
#     browser.get("http://www.baidu.com")


#
# def func(x):
#     return x + 1
# def test_answer():
#     assert func(3) == 4


