#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/8 11:25'

from util.dos_cmd import DosCmd


class Port:
    def port_is_used(self, port_num):
        """
        检测端口是否被占用，把未占用的端口添加到列表中
        :param port_num:
        :return:
        :param port_num:
        :return:
        """
        self.dos = DosCmd()
        result = self.dos.execute_cmd_result('netstat -ano | findstr {0}'.format(port_num))
        # 检测端口是否被占用，如果被占用有返回值
        if len(result) > 0:
            return True
        else:
            return False

    def create_port_list(self, start_port, device_list):
        """
        生成可用端口，如果端口已经被占用，就不生成
        :param start_port:
        :param device_list:
        :return:
        """
        port_list = []  # 生成可用端口
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) != True:  # 端口没有被占用返回None
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            return None
