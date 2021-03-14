#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/5/23 12:19'

import unittest

from business.home import Home


class HomeCaseTest(unittest.TestCase):
    '''首页自动化测试用例'''

    @classmethod
    def setUpClass(cls):
        cls.home_business = Home(0)

    def test_01_home_title(self):
        pass

    def test_02_get_home_number(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
