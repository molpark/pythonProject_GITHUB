# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 8:25
# @Author  : lys
# @Project : pythonProject
# @File    : testurllib.py
#一般需要用到的包
from bs4 import BeautifulSoup    ##网页解析获取数据
import re                        ##正则表达式 进行文字匹配
import urllib.request,urllib.error,urllib.parse  ##指定url,获取网页数据
import xlwt                         ##进行excel操作
import sqlite3                      ##进行SQLite数据库操作


# 获取一个get 请求
# response=urllib.request.urlopen("http://www.baidu.com")
# #读取requset返回值的内容,并进行转码(二进制文件utf8解析)
# #对获取到的网页源码进行utf-8解码
# print(response.read().decode('utf-8'))

#获取一个post 请求,模拟用户真实登录的情况
#分配一个data,用data 来封装post请求
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))

#超时要有一个计划性的准备
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e)


#响应头,返回状态
# response=urllib.request.urlopen("http://www.baidu.com",timeout=1)
# print(response.status)#状态码还会有404,500,418等情况(404:找不到,418:发现是爬虫,500返回错误)
# print(response.getheaders())
#单独获取header参数
#print(response.getheader("Server"))

#url='https://www.douban.com'
#url='http://httpbin.org/post'
url='http://www.baidu.com'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}
data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
req=urllib.request.Request(url=url,data=data,headers=headers,method='POST')
response=urllib.request.urlopen(req)
#print(response.read().decode('utf-8'))
html=response.read().decode('utf-8')
with open(r'C:\job\learning\pythonProject\venv\learn\爬虫\python爬虫和数据可视化\test2\baidu.html','w',encoding='utf-8') as f:
    f.write(str(html))



#豆瓣最主要是要提供一个header来模仿浏览器的访问
#提供浏览器的信息
# url='https://www.douban.com'
# headers={
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
# }
# req=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))