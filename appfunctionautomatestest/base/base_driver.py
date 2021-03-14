#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/5/15 12:03'

import time

from appium import webdriver

from util.warite_user_command import WriteUserCommand


class BaseDriver:
    def android_driver(self, i):
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_{0}'.format(i), 'deviceName')
        port = write_file.get_value('user_info_{0}'.format(i), 'port')
        capabilities = {
            "platformName": "Android",
            "deviceName": devices,
            "app": "C:/Users/Administrator/Desktop/lhapk/lh.apk",
            "appActivity": "com.royaleu.ckbd.activity.MainActivity",
            "noReset": "true",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:{0}/wd/hub".format(port), capabilities)
        time.sleep(5)
        return self.driver

    def ios_driver(self):
        """
        必须有mac和iphone手机
        :return:
        """
        pass

    def get_driver(self):
        pass

    def get_size(self):
        '''获取设备的屏幕尺寸'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_up(self):
        '''向上'''
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y, 1000)
