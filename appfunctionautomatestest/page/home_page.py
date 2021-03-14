#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/5/23 14:19'

from base.base_driver import BaseDriver
from base.base_get_web import GetWeb
from util.get_by_local import GetByLocal


class HomePage:
    """
    页面层
    """

    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)
        self.base_web_obj = GetWeb()  # 获取web端的公共类

    def get_home_element_common(self, comm_element, section=None):
        """
        公共方法
        :return:
        """
        return self.get_by_local.get_element(comm_element, section)
