# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 23:37
# @Author  : lys
# @Project : pythonProject
# @File    : log_004_记录变量数据.py

import logging
# logging.basicConfig(level=logging.INFO)
# logging.info('%s是傻逼','傻逼')
# sb='贱人'
# logging.info(f'{sb}是傻逼')
# logging.info('{}是傻逼'.format('日你码'))

#更改显示消息的格式
#这里levelname 还是固定格式,具体想知道参数有什么可以把(levelname)删了执行下就看到了
#但为了简单使用，你只需要 levelname （严重性）， message （事件描述，包括可变数据），也许在事件发生时显示。
#下面展示了一些公共信息
logging.basicConfig(format='%(asctime)s|%(filename)s:%(lineno)s|%(levelname)s|%(message)s',level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')


