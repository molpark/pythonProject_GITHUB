# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 17:59
# @Author  : lys
# @Project : pythonProject
# @File    : log_高级_001.py

'''
logging的高级应用
logging模块采用了模块化设计,主要包含四种组件:
1.Loggers:记录器,提供应用程序代码能直接使用的接口
2.Handlers:处理器,将记录器产生的日志发送至目的地
3.Filters:过滤器,提供更好的粒度控制,决定哪些日志会被输出
4.Formatters:格式化器,设置日志内容的组成结构和消息字段
'''
import logging

'''
# loggers记录器
# 1.提供应用程序的调用接口
logger=logging.getLogger(__name__)
#logger是单例
#2.决定日志记录的级别
logger.setLevel()
#3.将日志内容传递到相关联的handlers中
logger.addHandler()
logger.removeHandler()
'''

'''
Handles 处理器
他们将日志分发到不同的目的地.可以是文件,标准输出,邮件,或者通过socket.http等协议发送到任何地方
SteamHandler
标准输出stdout(如显示器)分发器
创建方法: sh=logging.StreamHandler(stream=None)
FileHandler
将日志保存到磁盘文件的处理器
创建方法:fh=logging.FileHandler(filename,mode='a',encoding=None,delay=False)
setFormatter():设置当前handler对象使用的消息格式
Handlers处理器常用的几个处理器:
    StreamHandler  --最常用
    FileHandler    --最常用
    BaseRotatingHandler
    RotatingFileHandler
    TimedRotatingFileHandler
    SMTPHandler    --邮件
'''

'''
Formatters格式
Formatter对象用来最终设置日志信息的顺序,结构,和内容
其构造方法为
ft=logging.Formatter.__init__(fmt=None,datefmt=None,style='%')
datefmt默认是%Y-%m-%d %H:%M%S 样式的
style参数默认为百分符%,这表示%(<dictionar key>)s格式的字符串
具体有哪些格式可以查看印象笔记
'''
