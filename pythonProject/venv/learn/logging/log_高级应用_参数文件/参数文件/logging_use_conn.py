# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 23:00
# @Author  : lys
# @Project : pythonProject
# @File    : logging_use_conn.py
import logging
import logging.config
#配置文件的方式来处理日志
logging.config.fileConfig('logging_sp.conf')
#记录器 不传参默认是'root'
root_logger=logging.getLogger('root')
root_logger.debug("this is rootdebug")
root_logger.info("this is rootinfo")

logger=logging.getLogger('applog')   #可以自己定一个名字
#打印日志的代码
#按照上面设置即会生成文件日志又会在窗口输出日志
logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is ")


##如何使用logger,在日常开发代码过程中
a='abc'
try:
    int(a)
except Exception as e:
    #logger.error(e)
    #抛出的异常要用logger.exception来输出,主要是方便你在日志和控制台更方便的发现报错信息
    logger.exception(e)


