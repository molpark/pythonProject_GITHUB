# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 22:33
# @Author  : lys
# @Project : pythonProject
# @File    : 05模拟登录qq空间.py
from selenium import webdriver
import time
#导入动作链对应的类
from selenium.webdriver import ActionChains
bro=webdriver.Chrome(executable_path=r'C:\software\Anaconda3\Scripts\chromedriver.exe')

bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
div=bro.find_element_by_id('switcher_plogin')
# action=ActionChains(bro)
# action.click(div)
# action.perform()
div.click()
username=bro.find_element_by_id('u')
username.send_keys('897020846')
password=bro.find_element_by_id('p')
password.send_keys('APPLEair90120405')
# denglu_click=bro.find_element_by_css_selector('.login_button')
denglu_click=bro.find_element_by_id('login_button')
denglu_click.click()
time.sleep(10)
bro.quit()