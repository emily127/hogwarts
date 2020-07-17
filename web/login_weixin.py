#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-17 10:32
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base:
    def setup(self):
        option = Options()
        #和浏览器打开的调试窗口进行通信
        #浏览器要使用./Google\ Chrome --remote-debugging-port=9222 开启调试
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

#使用cookie登录
class TestLogin(Base):
    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        #获取cookie
        #print(self.driver.get_cookies())
        #shelve是Python自带的数据库，open一个库时，如果存在，打开已有的；如果不存在，新建一个库
        db = shelve.open("cookies")

        #cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850168879042'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '36FIX2bBtQXdAuPJR5F0etNKWy8mo-Ir_Ioxrprkyh5pAhM6SbGMjG46eSGByU6WDT7CcF3nPYuJKU1cQIDPoKD0U1FBAk10_PnXU6y4lfV8atogDO3TYbi3gKXXeTgbbcsdMDipn5oVAmlQNVfysZruxhIECCvULycQOwQw6c98L_JIGo9-8dxoPB6uWVDH1L2GZpHh2RT2CVetv_hXOfXqC0Ec7hyrZIgRMxqgQOed-GV9wo0kTM0U1PbbDo7pwdiapudhIUqkrw7T5BDB2w'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850168879042'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325087155764'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '5uLUoMN9DyaoZRvyeOQl2zWqoHlbE7p3Cd4of8fJM73enTf2h3r3PSmuPPCd4veb'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7933014'}, {'domain': 'work.weixin.qq.com', 'expiry': 1594995833, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '6kkgn3t'}, {'domain': '.qq.com', 'expiry': 1595055694, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.448248546.1594964754'}, {'domain': '.qq.com', 'expiry': 1658041294, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1025196492.1594964754'}, {'domain': '.work.weixin.qq.com', 'expiry': 1594995833, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '86152e8d104a4d7aeaed94f72264b8d9c4ffaea19091c26b5f97518390fd4e52'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1626504793, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594964706,1594967052,1594967307,1594968794'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'gXrQapWX4/'}, {'domain': '.work.weixin.qq.com', 'expiry': 1597564117, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594968794'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '24513422633192868'}, {'domain': '.qq.com', 'expiry': 1594973074, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '8060775424'}]
        # db["cookies"] =cookies
        cookies = db["cookies"]
        for cookie in cookies:
            #如果cookie 中的时效字段在字典中，就删掉
            # if "expiry" in cookie.keys():
            #     cookie.pop("expiry")
            #把字典加入到driver的cookie中
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        time.sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        time.sleep(3)
        db.close()
