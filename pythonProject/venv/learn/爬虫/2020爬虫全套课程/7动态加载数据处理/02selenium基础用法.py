# -*- coding: utf-8 -*-
# @Time    : 2022/5/19 17:13
# @Author  : lys
# @Project : pythonProject
# @File    : 02selenium基础用法.py
import time

from selenium import webdriver
from lxml import etree
#实例化一个浏览器对象(传入浏览器的驱动)
bro=webdriver.Chrome(executable_path=r'C:\software\Anaconda3\Scripts\chromedriver.exe')
#让浏览器发起一个指定url对应请求
bro.get('https://www.gushiwen.cn/')
#page_source获取浏览器当前页面的页面源码数据
page_text=bro.page_source
#解析名称
tree=etree.HTML(page_text)
b_list=tree.xpath('/html/body/div[2]/div[1]/div[4]/div[1]/p[1]/a/b/text()')[0]
print(b_list)
time.sleep(2)
#关闭浏览器
bro.quit()