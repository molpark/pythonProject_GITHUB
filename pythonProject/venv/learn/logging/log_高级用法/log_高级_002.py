# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 19:03
# @Author  : lys
# @Project : pythonProject
# @File    : log_高级_002.py
import logging
#编程的方式来写一下高级的写法
#记录器 不传参默认是'root'
logger=logging.getLogger('app.cn.cccb.applog')   #可以自己定一个名字
logger.setLevel(logging.DEBUG)  ##记录器只有设置等级越低,在处理器的时候才会有选择空间.如果记录器给了默认的warning就算处理器选了info,也不会输出info日志
#print(logger)
#print(logger.name) --root
#print(type(logger))

#处理器
#显示器handler
consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
#文件handler#不指定级别,默认使用logger记录器定的级别,比如本脚本目前定的logger 的级别就是INFO
fileHandle=logging.FileHandler(filename='addFileDemo.log',encoding='utf-8',mode='w')
fileHandle.setLevel(logging.INFO)
#formatter格式
#注意%(levelname)8s 这边给了个8s,意思就是这个s字符串固定给8位的空格,这是为了日志对齐用的(-8 就是左对齐)
formatter=logging.Formatter('%(asctime)s|%(filename)10s:%(lineno)4s|%(levelname)-8s|%(message)s')

#给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandle.setFormatter(formatter)

#记录器设置处理器(这个记录器用两个处理器分别往不同地方输出)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandle)

#定义一个过滤器
#过滤哪些要输出哪些不要输出 ,意思就是要哪个看哪个logger生成的日志
#flt=logging.Filter('cn.cccb') #匹配规则是看我们定义loggername的时候的前缀,只匹配开头但验证下来还要看分隔符 我们现在定义的logger 叫 applog,
flt2=logging.Filter('app') #
#关联过滤器
#logger.addFilter(flt)
#logger.addFilter(flt2)
#还可以给处理器增加过滤器,比如此时给filehandler加,那么file日志可能会无法有日志输入进去
fileHandle.addFilter(flt2)

#打印日志的代码
#按照上面设置即会生成文件日志又会在窗口输出日志
logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is ")
logger.exception()

