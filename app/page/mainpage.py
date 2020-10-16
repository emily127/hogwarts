#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-28 14:01 

'''
主页面
'''
from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.contactlistpage import ContactListPage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    '''
    进入通讯录
    '''
    contact_list = (MobileBy.XPATH,"//android.widget.TextView[@text='通讯录']")
    def goto_contactlist(self):
        # self.driver.find_element(MobileBy.XPATH,"//android.widget.TextView[@text='通讯录']").click()
        self.find_and_click(self.contact_list)
        return ContactListPage(self.driver)