# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 12:07
# @Author  : lys
# @Project : pythonProject
# @File    : 4协程.py

#P45 弹幕提示先从P83看到底
import asyncio

async def request(url):
    print('正在请求'+url)
    print('请求成功'+url)
    return url
#async修饰的函数,调用之后返回的一个协程对象
c=request('www.baidu.com')
#d=request('www.haha.com')

#创建一个事件循环对象
# loop=asyncio.get_event_loop()
# #讲协程对象注册到loop中,然后就可以启动事件循环(loop)
# loop.run_until_complete(c)

#弹幕意思不需要用loop对象,直接润
#asyncio.run(c)

#task 的使用
# loop=asyncio.get_event_loop()
# #基于loop创建了一个task对象
# task=loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

#future的使用和task的区别只是使用方法上有区别,用哪种都行看使用习惯
# loop=asyncio.get_event_loop()
# future=asyncio.ensure_future(c)
# future_d=asyncio.ensure_future(d)
# print(future)
# loop.run_until_complete(future)
# loop.run_until_complete(future_d)
# print(future)

#绑定回调
def callbak_func(task):
    #result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())
#绑定回调
loop=asyncio.get_event_loop()
task=asyncio.ensure_future(c)
#讲回调函数绑定到任务对象中
task.add_done_callback(callbak_func)
loop.run_until_complete(task)
