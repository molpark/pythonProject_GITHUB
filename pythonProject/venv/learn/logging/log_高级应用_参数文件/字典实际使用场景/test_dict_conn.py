# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 23:44
# @Author  : lys
# @Project : pythonProject
# @File    : test_dict_conn.py
import logging

#使用方法
import logging
from logging_dict_conf import load_my_logging_cfg
load_my_logging_cfg()
mylog=logging.getLogger('your_app_name')

def test1():
    try:
        print(1 / 0)
    except Exception as e:
        mylog.exception(str(e))  # 将异常写入日志
test1()
