# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 23:11
# @Author  : lys
# @Project : pythonProject
# @File    : log_002_记录日志到文件.py

import logging

#filemode=w 和write 的模式一样会覆盖写
logging.basicConfig(filename='logfile/test002_log.log', level=logging.DEBUG, filemode='w')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


