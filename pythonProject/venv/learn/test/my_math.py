# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 20:13
# @Author  : lys
# @Project : pythonProject
# @File    : my_math.py


import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')
try:
    print(1 / 0)
except Exception as e:
    logging.info('error:'+str(e))
    logging.error(str(e))
logging.info('The division succeeded')
logging.info('Ending program')

def ts():
    pass