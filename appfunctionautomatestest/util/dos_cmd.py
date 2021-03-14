#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/8 11:26'

import os


class DosCmd:
    """
    获取移动设备的devices
    """

    def execute_cmd_result(self, command):
        result_list = []
        # 执行传入的command命令，然后将结果保存到result中,类型为list
        result = os.popen(command).readlines()
        for i in result:
            if i.strip() == "": continue
            result_list.append(i.strip())
        return result_list

    def execute_cmd(self, command):
        os.system(command)  # 执行命令
