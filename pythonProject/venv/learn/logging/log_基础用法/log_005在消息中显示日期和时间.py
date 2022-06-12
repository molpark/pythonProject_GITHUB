# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 9:32
# @Author  : lys
# @Project : pythonProject
# @File    : log_005在消息中显示日期和时间.py

'''
发现一个特殊的规则,logging.basicConfig 只认第一次的设置.后面不管是新添设置还是修改设置,都对原设置无效
而且basicconfig 的设置必须放在最前面的地方,不然如果已经有了logging.warning()再去写设置没用了
'''

import logging
#logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
#logging.warning('is when this event was logged')

#日期/时间显示的默认格式（如上所示）类似于 ISO8601 或 RFC 3339 。 如果你需要更多地控制日期/时间的格式，请为 basicConfig 提供 datefmt 参数，如下例所示:
#datefmt 参数的格式与 time.strftime() 支持的格式相同
import logging
#logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logging.warning('this is a warning')