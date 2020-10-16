#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-28 14:03 

'''
通讯录列表页面
'''
from app.page.addmemberpage import AddMemberPage
from app.page.basepage import BasePage


class ContactListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addmember = "添加成员"
    def addcontact(self):
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().text("添加成员").'
        #                                                 'in(0));').click()
        self.find_by_scroll(self.addmember).click()
        return AddMemberPage(self.driver)

    def searchcontact(self):
        pass