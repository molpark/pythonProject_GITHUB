# -*- coding: utf-8 -*-
# @Time    : 2022/3/27 20:01
# @Author  : lys
# @Project : pythonProject
# @File    : spider_001.py

#一般需要用到的包
from bs4 import BeautifulSoup    ##网页解析获取数据
import re                        ##正则表达式 进行文字匹配
import urllib.request,urllib.error,urllib.parse  ##指定url,获取网页数据
import xlwt                         ##进行excel操作
import sqlite3                      ##进行SQLite数据库操作


def main():
    baseurl='https://movie.douban.com/top250?start='
    savepath=r".\豆瓣电影TOP250.xls"
    #1.爬取网页
    datalist=getdata(baseurl)


    #3.保存数据
    #savedata(savepath)
    askurl(baseurl)


#爬取网页
def getdata(baseurl):
    datalist=[]
    for i in range(0,10):   #调用获取页面信息的函数,10次
        url=baseurl+str(i*25)
        html=askurl(url)    #保存获取到的网页源码
        # 2.逐一解析数据


#得到指定一个URL的网页内容
def askurl(baseurl):
    #用户代理,表示告诉豆瓣服务器,我们是什么类型的机器,浏览器(本质是告诉浏览器,我们可以接收什么水平的文件)
    #模拟浏览器头部信息,向豆瓣服务器发送消息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    req=urllib.request.Request(url=baseurl,headers=headers)
    html=''
    try:
        response=urllib.request.urlopen(req)
        html=response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html

#保存数据
def savedata(savepath):
    pass


if __name__ == '__main__':
    main()