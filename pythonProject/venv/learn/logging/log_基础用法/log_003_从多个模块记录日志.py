# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 23:27
# @Author  : lys
# @Project : pythonProject
# @File    : log_003_从多个模块记录日志.py


import logging
from log_003_从多个模块记录日志2 import test2 as ts2

def main():
    logging.basicConfig(filename='logfile/test003_log.log', filemode='w', level=logging.INFO)
    logging.info('logging start')
    ts2()
    logging.info('logging finish')

if __name__ == '__main__':
    main()