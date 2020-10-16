#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-29 09:46
'''
存放基本的方法
初始化driver
find查找元素
'''
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self,driver:WebDriver = None):
        self.driver = driver

    def find(self,locator):
        logging.info(f'find: {locator}')
        return self.driver.find_element(*locator)

    #查找元素并点击
    def find_and_click(self,locator):
        logging.info('click')
        self.find(locator).click()
    #查找元素并传值
    def find_and_sendkeys(self,locator,text):
        logging.info(f'send_keys: {text}')
        self.find(locator).send_keys(text)
    #滚动查找
    def find_by_scroll(self,text):
        logging.info('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).instance(0)).'
                                        f'scrollIntoView(new UiSelector().text("{text}").'
                                        'instance(0));')

    #显式等待的封装
    def webdriver_wait(self,locator,timeout=10):
        logging.info(f'webwait: {locator}, timeout: {timeout}')
        ele = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return ele
    #返回操作
    def back(self,num=1):
        logging.info(f'back: {num}')
        for i in range(num):
            self.driver.back()

