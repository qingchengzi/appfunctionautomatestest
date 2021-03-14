#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/5/23 14:19'

from page.home_page import HomePage


class HomeHandle:
    """
    操作层
    """

    def __init__(self, i):
        self.home_page = HomePage(i)
        self.driver = self.home_page.driver

    def get_home_title_text(self):
        """
        获取首页title
        :return:
        """
        res_title = self.home_page.get_home_element_common("title_id", section="home_element").text
        return res_title
