#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-28 15:05 
#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi
# ide: pycharm
# @Time: 2020-07-28 15:03
# with open('data/addcontact.yml') as f:
#     data =yaml.safe_load(f)
import time

import pytest
import yaml
from appium import webdriver

# from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

with open('data/addcontact.yml') as f:
    data = yaml.safe_load(f)
class Testcontact:
    """
    添加联系人用例设计
    1、打开应用
    2、点击通讯录
    3、点击添加成员
    4、手动输入添加
    5、输入【用户名】,性别，手机号
    6、点击保存
    7、验证添加成功
    """
    def setup(self):
        despire_cap = {
          "platformName": "android",
          "deviceName": "emulator-5554",
          "appPackage": "com.tencent.wework",
          "appActivity": ".launch.LaunchSplashActivity",
          "noReset": True,
          #跳过uiautomator2的安装
          "skipServerInstallation": "true",
          # 跳过设备初始化
          "skipDeviceInitialization": "true",
          "settings[waitForIdleTimeout]": 0,
          #启动之前不停止app
          # "dontStopAppOnReset": "true"
          }
        #与server建立连接，初始化一个driver，创建session,返回一个session
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",despire_cap)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize('name,gender,phone',data)
    def test_addcontact(self,name,gender,phone):
        # name = '自动化2'
        # gender = '女'
        # phone = '13412345678'
        self.driver.find_element(MobileBy.XPATH,"//android.widget.TextView[@text='通讯录']").click()
        #联系人较多，需要滚动查找'添加成员'的按钮
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                          'scrollable(true).instance(0)).'
                                                          'scrollIntoView(new UiSelector().text("添加成员").'
                                                         'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//android.widget.TextView[@text='手动输入添加']").click()
        #设置姓名
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']").send_keys(name)
        #设置性别
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.TextView' and @text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        #设置手机号
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys(phone)
        #设置部门
        self.driver.find_element(MobileBy.XPATH,"//*[@text='设置部门']").click()
        #点击确定
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定(1)']").click()
        #点击保存
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/h9w").click()

        #验证成功,Toast,需要加显式等待
        #self.driver.find_element(MobileBy,"//*[@class='android.widget.Toast']").text
        ele = WebDriverWait(self.driver,10).until(lambda x:x.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']"))
        result = ele.text
        assert '成功' in result
        self.driver.back()
    # @pytest.mark.parametrize('delname',data)
    # def test_delcontact(self,delname):
    #     """
    #     删除联系人
    #     1、打开应用
    #     2、点击通讯录
    #     3、找到要删除的联系人
    #     4、进入联系人界面
    #     5、点击右上角三个点进入个人信息页面，编辑成员
    #     6、删除联系人
    #     7、确认删除
    #     8、验证删除成功
    #     :return:
    #     """
    #     # delname = '测试2'
    #     #点击通讯录
    #     self.driver.find_element(MobileBy.XPATH,"//android.widget.TextView[@text='通讯录']").click()
    #     #搜索姓名
    #     self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/h9z").click()
    #     self.driver.find_element(MobileBy.XPATH,"//*[@text='搜索']").send_keys(delname)
    #     time.sleep(5)
    #     #判断查询长度
    #     ele = self.driver.find_elements(MobileBy.XPATH,f'//*[@text="{delname}"]')
    #     if len(ele) <2:
    #         print('没有这个联系人')
    #         return
    #     ele[1].click()
    #     #点击右上角三个点
    #     self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/h9p").click()
    #     #点击编辑成员
    #     self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
    #     #滚动查找'删除成员'
    #     self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
    #                                                     'scrollable(true).instance(0)).'
    #                                                     'scrollIntoView(new UiSelector().text("删除成员").'
    #                                                     'instance(0));').click()
    #     #点击确定
    #     self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
    #     time.sleep(2)
    #     #验证搜索的姓名返回只有1个，即删除成功
    #     ele_del = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{delname}"]')
    #     assert len(ele_del) == 1
