#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-28 14:07
from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    name_locator = (MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']")
    gender_locator = (MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
    male_locator = (MobileBy.XPATH,'//*[@text="男"]')
    female_locator = (MobileBy.XPATH,"//*[@text='女']")
    phone_locator = (MobileBy.XPATH,"//*[@text='手机号']")
    save_locator = (MobileBy.ID,"com.tencent.wework:id/h9w")
    def set_name(self,name):
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']").send_keys(name)
        self.find_and_sendkeys(self.name_locator,name)
        return self
    def set_gender(self,gender):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        self.webdriver_wait(self.male_locator)

        self.find_and_click(self.gender_locator)
        if gender == '男':
            # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.TextView' and @text='男']").click()
            self.find_and_click(self.male_locator)
        else:
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click(self.female_locator)
        return self
    def set_phone(self,phone):
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys(phone)
        self.find_and_sendkeys(self.phone_locator,phone)
        return self
    # def set_branch(self):
    #     self.driver.find_element(MobileBy.XPATH,"//*[@text='设置部门']").click()
    #     return self

    def click_save(self):
        from app.page.addmemberpage import AddMemberPage

        # self.driver.find_element(MobileBy.XPATH, "//*[@text='确定(1)']").click()
        # 点击保存
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9w").click()
        self.find_and_click(self.save_locator)
        return AddMemberPage(self.driver)
