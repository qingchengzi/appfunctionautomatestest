#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/5/23 12:28'

from handled.home_handle import HomeHandle


class Home:
    '''
    【业务层】
    '''

    def __init__(self, i):
        self.home_handle = HomeHandle(i)

    def get_home_title(self):
        '''获取home页面的title'''
        res_title = self.home_handle.get_home_title_text()
        return res_title.strip()
