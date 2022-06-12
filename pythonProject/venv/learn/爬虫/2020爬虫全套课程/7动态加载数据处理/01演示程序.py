# -*- coding: utf-8 -*-
# @Time    : 2022/5/19 17:13
# @Author  : lys
# @Project : pythonProject
# @File    : 01演示程序.py
import time

from selenium import webdriver
from lxml import etree
#实例化一个浏览器对象(传入浏览器的驱动)
bro=webdriver.Chrome(executable_path=r'C:\software\Anaconda3\Scripts\chromedriver.exe')
