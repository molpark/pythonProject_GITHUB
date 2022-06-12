# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 10:37
# @Author  : lys
# @Project : pythonProject
# @File    : 同步爬虫.py
import time

import requests
import threading
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
url=(
    'https://www.gushiwen.cn/',
    'https://so.gushiwen.cn/shiwens/',
    'https://so.gushiwen.cn/mingjus/'
)
def get_text(url):
    print('正在爬取',url)
    #get 方法是一个阻塞的方法因为需要执行的时间较长
    response=requests.get(url=url,headers=headers)
    if  response.status_code==200:
        return response.text
def parse_text(text):
    print('响应数据的长度为',len(text))
def main(url):
    parse_text(get_text(url))


def threading_parse(tab):
    lines=tab
    for i in lines:
        threading.Thread(target=main, args=(i,)).start()
    #好像执行过快就不需要join
    # for it in lines:
    #     threading.Thread(target=main, args=(it,)).join()


if __name__ == '__main__':
    #同步
    for i in url:
        main(i)
    #threading 方法
    threading_parse(url)