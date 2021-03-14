#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/5/18 15:10'

import configparser, os


class ReadIni:
    """
    读取配置文件LocalElement.ini
    """

    def __init__(self, file_path=None):

        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if file_path == None:
            self.file_path = "{0}/config/LocalElement.ini".format(dir_path)
        else:
            self.file_path = "{0}{1}".format(dir_path, file_path)

        self.data = self.read_ini()

    def read_ini(self):
        """
        读取.ini
        :return:
        """
        read_init = configparser.ConfigParser()
        read_init.read(self.file_path, encoding="utf-8")
        return read_init

    # 通过参数key获取对应的value
    def get_value(self, key, section=None):
        if section == None:
            section = "home_element"
        try:
            value = self.data.get(section, key)
            return value
        except:
            value = None

        return value


if __name__ == '__main__':
    obj_read = ReadIni()
    print(obj_read.get_value("username"))
