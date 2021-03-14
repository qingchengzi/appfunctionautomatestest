#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/5/17 17:38'

from util.read_init import ReadIni


class GetByLocal:
    """
    获取定位信息
    """

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, section=None):
        read_ini = ReadIni()
        local = read_ini.get_value(key, section)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'pluralclassName':
                    return self.driver.find_elements_by_class_name(local_by)
                elif by == 'uiselector':
                    return self.driver.find_element_by_android_uiautomator('new UiSelector().{0}'.format(local_by))
                elif by == 'uiselectorsss':
                    return self.driver.find_elements_by_android_uiautomator('new UiSelector().{0}'.format(local_by))
                elif by == 'ids':
                    return self.driver.find_elements_by_id(local_by)
                elif by == 'webcss':  # html5,css定位
                    return self.driver.find_element_by_css_selector(local_by)
                elif by == 'webxpath':  # html5 xpath定位
                    return self.driver.find_element_by_xpath(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                return None
        else:
            return None
