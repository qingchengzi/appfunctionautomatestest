#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/8 10:16'

import time
import unittest

from HTMLTestRunner import HTMLTestRunner


def run_test_suit():
    """
    运行测试用例集
    :return:
    """
    return unittest.defaultTestLoader.discover("./testsuite", pattern="*_test.py")


def app_init():
    pass


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    title_time = time.strftime("%Y-%m-%d %H:%M")
    report_file = './report/{0}app.html'.format(now)
    with open(report_file, "wb") as fw:
        runner = HTMLTestRunner(
                stream=fw,
                title="{0}港湾置业app端自动化测试报告".format(title_time),
                description="安卓1.6.0版本",
                verbosity=2,
        ).run(run_test_suit())
