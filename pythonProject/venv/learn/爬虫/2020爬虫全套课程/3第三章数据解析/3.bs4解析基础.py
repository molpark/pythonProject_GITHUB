# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 17:48
# @Author  : lys
# @Project : pythonProject
# @File    : 3.bs4解析基础.py
import requests
from bs4 import BeautifulSoup
import lxml

if __name__ == '__main__':
    #将本地的html文档中的数据加载到该对象中
    fp=open('./sogou.html','r',encoding='utf-8')
    soup=BeautifulSoup(fp,'lxml')
    #print(soup)
    #print(soup.a) #soup.tagName 返回的是html中第一次出现的tagName标签
    #print(soup.div)
    res=soup.find('div')  #等同于soup.div
    #print(res)  # 等于print(soup.div)
    res=soup.find('div',attrs='wrapper')   #或者 class_='wrapper'这的class 需要带下划线
    #print(res)
    res=soup.find_all('a')   #返回的是符合需求的所有标签,返回的是一个列表
    res=soup.select('.wrapper') # select('某种选择器(id,class,标签....选择器)'),返回的是一个列表
    res=soup.select('.top-nav>ul>li>a')[0] #select 层级选择器 >表示的是一个层级
    res = soup.select('.top-nav>ul a')[0]  # select 层级选择器 空格 表示的是多个层级
    res = soup.select('.top-nav>ul a')[0].get_text() #获取标签中的文本方法get_text(),text,string
    res=soup.find('div',class_='wrapper').string   #返回的是直系下的文本内容
    res = soup.find('div', class_='wrapper').get_text() #返回的是整个div下的文本内容
    res = soup.select('.top-nav>ul a')[0]['href']  #返回的是该a标签中对应的href 属性值
    print(res)
