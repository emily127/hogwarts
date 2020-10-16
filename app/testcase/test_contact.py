#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-07-28 14:10
import pytest
import yaml

from app.page.app import App

with open('../data/addcontact.yml') as f:
    data = yaml.safe_load(f)
class TestContact:
    def setup_class(self):
        self.app =App()
    def setup(self):
        self.main = self.app.start().goto_main()
    def teardown_class(self):
        self.app.stop()
    def teardown(self):
        self.app.back(5)
    @pytest.mark.parametrize('name,gender,phone',data)
    def test_addcontact(self,name,gender,phone):
        # name = '自动化11'
        # gender = '男'
        # phone = '15812345676'
        mypage = self.main.goto_contactlist().addcontact().add_menual().set_name(name).set_gender(gender).set_phone(phone).click_save()
        text = mypage.get_toast()
        assert '成功' in text
        self.app.back()