# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 23:10
# @Author  : lys
# @Project : pythonProject
# @File    : log_001_一个简单的例子.py
import logging
#默认的日志输出界别为warning
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything

#使用baseConfig()来指定日志输出级别
logging.basicConfig(level=logging.INFO)
logging.info('I told you so')

