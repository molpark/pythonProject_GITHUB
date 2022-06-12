# -*- coding: utf-8 -*-
# @Time    : 2022/5/19 16:17
# @Author  : lys
# @Project : pythonProject
# @File    : 6多任务异步协程02.py

import requests
import asyncio
import time
#环境安装 pip install aiohttp
#使用该模块中的ClientSession
import aiohttp
start=time.time()
urls=['http://127.0.0.1:5000/bobo ','http://127.0.0.1:5000/tom ','http://127.0.0.1:5000/jay']

async def get_page(url):
    print(f'正在现在{url}')
    #request.get是基于同步,必须使用基于异步的网络请求模块进行指定url的请求发送
    #response=requests.get(url=url)
    #print(response.text)
    # aiohttp :基于异步网络请求的模块
    async with aiohttp.ClientSession() as session:
        #get(), post()
        #headers
        #params,data
        #proxy='http://ip:port'
        async with await session.get(url=url) as response:
            #text()方法返回字符串形式的响应数据
            #read()返回的二进制形式的响应数据
            #json()返回的是json对象
            page_text=await response.text()
            print(page_text)
    print(f'下载完毕{page_text}')

tasks=[]
for url in urls:
    c=get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end=time.time()
print('总耗时',end-start)