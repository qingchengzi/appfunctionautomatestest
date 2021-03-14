#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/8 11:55'

import yaml
import os


class WriteUserCommand:
    def __init__(self):
        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_yaml = "{0}/config/userconfig.yaml".format(dir_path)

    def read_data(self):
        """
        读取加载yaml文件
        :return:
        """
        with open(self.file_yaml) as fr:
            data = yaml.load(fr)

        return data

    def get_value(self, key, port):
        '''
        获取value，获取某一行
        :param key:
        :return:
        '''
        data = self.read_data()
        value = data[key][port]
        return value

    def clear_data(self):
        """
        清空数据
        :return:
        """
        with open(self.file_yaml, "w") as fr:
            fr.truncate()  # 内置方法清空数据
        fr.close()

    def write_data(self, i, device, bp, port):
        """
        写入数据
        :param i: 第几个
        :param device: 设备id
        :param bp:
        :param port:
        :return:
        """
        data = self.join_data(i, device, bp, port)
        with open(self.file_yaml, "a") as fr:
            yaml.dump(data, fr)

    def join_data(self, i, device, bp, port):
        data = {
            "user_info_{0}".format(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def get_file_lines(self):
        """
        统计config目录userconfig.yaml中共多少条数据
        :return:
        """
        data = self.read_data()
        return len(data)


if __name__ == '__main__':
    obj = WriteUserCommand()
    obj.read_data()
