#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/8 11:44'

import os

rest = os.popen("netstat -ano | findstr 80").readlines()

# print(rest)

ret = os.system("netstat -ano | findstr 80")
print(ret)
