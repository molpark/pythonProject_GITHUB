# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 13:44
# @Author  : lys
# @Project : pythonProject
# @File    : selenium其他自动化操作.py

from selenium import webdriver
import time
bro=webdriver.Chrome(executable_path=r'C:\software\Anaconda3\Scripts\chromedriver.exe')

bro.get('https://www.taobao.com/')
#在搜索框输入关键词
#标签定位
#根据id定位
search_input=bro.find_element_by_id('q')
search_input.send_keys('Iphone')
time.sleep(2)
#执行一组js程序滚轮
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(5)
#点击搜索按钮
#btn=bro.find_element_by_class_name('btn-search')   #和下面一样
btn=bro.find_element_by_css_selector('.btn-search')
btn.click()
#切换页面
bro.get('https:www.baidu.com')
time.sleep(2)
#页面回退
bro.back()
time.sleep(2)
#页面前进
bro.forward()
time.sleep(5)


bro.quit()