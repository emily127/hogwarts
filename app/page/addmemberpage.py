#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-28 14:06
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.page.basepage import BasePage

'''
添加成员页
'''
class AddMemberPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addmenual = (MobileBy.XPATH,"//android.widget.TextView[@text='手动输入添加']")
    webdriver_locator = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
    def add_menual(self):
        from app.page.contactaddpage import ContactAddPage

        # self.driver.find_element(MobileBy.XPATH,"//android.widget.TextView[@text='手动输入添加']").click()
        self.find_and_click(self.addmenual)

        return ContactAddPage(self.driver)
    def get_toast(self):
        # ele = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        element = self.webdriver_wait(self.webdriver_locator)
        result = element.text
        return result
        # assert '成功' in result
        # self.driver.back()