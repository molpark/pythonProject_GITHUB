# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 18:47
# @Author  : lys
# @Project : pythonProject
# @File    : 01.requests第一血.py
#--需求:爬取搜狗首页的页面数据

import requests
if __name__ == '__main__':
    #1.指定url
    url='https://www.sogou.com/'
    #2.发起请求
    #get方法会返回一个响应对象
    response=requests.get(url=url)
    #3.获取响应数据 text返回的是字符串形式的响应数据
    page_text=response.text
    print(page_text)
    #4.持久化存储
    with open('sogou.html', 'w', encoding='utf-8') as f:
        f.write(page_text)
    print('爬取数据结束')
