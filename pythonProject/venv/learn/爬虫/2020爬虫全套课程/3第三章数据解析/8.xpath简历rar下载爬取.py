# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 22:52
# @Author  : lys
# @Project : pythonProject
# @File    : 8.1xpath简历rar下载爬取.py
from lxml import etree
import requests

if __name__ == '__main__':

    url='https://sc.chinaz.com/jianli/free_1.html'
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response=requests.get(url=url,headers=headers)
    response.encoding='gbk'
    page_text=response.text
    print(page_text)  ##页面无法下载到想要的html,html中显示页面不存在
    parser=etree.HTMLParser(encoding='utf-8')
    r=etree.HTML(page_text,parser=parser)
    jl_url_list=r.xpath('//*[@id="container"]/div')
    print(jl_url_list)
    for i in jl_url_list:
        jl_url=i.xpath('./a/@href')
        print(jl_url)


