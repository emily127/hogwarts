#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-28 13:52



'''
用来存放App应用常用的方法，例如：
启动app
关闭app
停止app
进入首页
'''
from appium import webdriver

from app.page.basepage import BasePage
from app.page.mainpage import MainPage


class App(BasePage):

    def start(self):
        '''
        启动app
        :return:
        '''
        #第一次调用start()方法时driver为None
        if self.driver == None:
            despire_cap = {
                "platformName": "android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": True,
                # 跳过uiautomator2的安装
                "skipServerInstallation": "true",
                # 跳过设备初始化
                "skipDeviceInitialization": "true",
                "settings[waitForIdleTimeout]": 0,
                # 启动之前不停止app
                # "dontStopAppOnReset": "true"
            }
            # 与server建立连接，初始化一个driver，创建session,返回一个session
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", despire_cap)
        #launch_app()这个方法不需要任何参数，会自动启动起来despire_cap里的activity
        #start_activity(packagename,activityname)可以启动其他的应用页面
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        '''
        重启app
        :return:
        '''
        self.driver.close()
        self.driver.launch()
        return self

    def stop(self):
        '''
        停止app
        :return:
        '''
        self.driver.quit()


    def goto_main(self):
        '''
        进入首页
        :return:
        '''
        return MainPage(self.driver)
