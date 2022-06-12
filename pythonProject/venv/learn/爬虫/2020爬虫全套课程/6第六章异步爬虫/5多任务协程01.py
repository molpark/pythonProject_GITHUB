# -*- coding: utf-8 -*-
# @Time    : 2022/5/19 14:44
# @Author  : lys
# @Project : pythonProject
# @File    : 5多任务协程01.py

import asyncio
import time

async def request(url):
    print(f'正在下载{url}')
    #在异步协程中如果出现了同步模块相关的代码,那么就无法实现异步
    #time.sleep(2)
    # 当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print(f'下载完毕{url}')

start=time.time()
url=['www.baidu.com','www.sougoou.com','www.doubanjiang.com']

#任务列表:存放多个任务对象
task_list=[]

for i in url:
    c=request(i)
    task = asyncio.ensure_future(c)
    task_list.append(task)
loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(task_list))
print(time.time()-start)