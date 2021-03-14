#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/8 11:24'


import threading
import time

from util.dos_cmd import DosCmd
from util.port import Port
from util.warite_user_command import WriteUserCommand


class Server():
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommand()
        self.obj_port = Port()

    def get_devices(self):
        """
        获取设备信息且进行处理
        例如:127.0.0.1:21503/t device
        :return:127.0.0.1:21503 device
        """
        devices_list = []
        result_list = self.dos.execute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def kill_server(self):
        """
        查看服务命令:tasklist | find "node.exe"
        :return:
        """
        server_list = self.dos.execute_cmd_result('tasklist | find "node.exe"')  # 查看是否开启node.exe服务
        if len(server_list) > 0:
            self.dos.execute_cmd('taskkill -F -PID "node.exe"')

    def create_port_list(self, start_port):
        """
        创建可用端口
        :return:
        """
        port_list = self.obj_port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        """
        为接入的每台设备拼接执行命令:
        appium -p 4700 -bp 4701 -U 127.0.0.1:21503
        :param i:
        :return:
        """
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        command = "appium -p {0} -bp {1} -U {2} --no-reset --session-override".format(appium_port_list[i],
                                                                                      bootstrap_port_list[i],
                                                                                      device_list[i])
        command_list.append(command)
        self.write_file.write_data(i, device_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))
        return command_list

    def start_server(self, i):
        """
        执行命令，启动服务
        :param i:
        :return:
        """
        self.start_list = self.create_command_list(i)
        self.dos.execute_cmd(self.start_list[0])

    def main(self):
        self.kill_server()  # 杀进程
        self.write_file.clear_data()  # 清空yaml中数据
        print(len(self.device_list))
        try:
            for i in range(len(self.device_list)):  # 连接这台机器的所有设备
                appium_start = threading.Thread(target=self.start_server, args=(i,))
                appium_start.start()
                time.sleep(15)
        except Exception as error:
            print("没有可用设备")


if __name__ == '__main__':
    obj = Server()
    obj.main()

