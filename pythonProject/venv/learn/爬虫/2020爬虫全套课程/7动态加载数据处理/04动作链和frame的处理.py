# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 14:50
# @Author  : lys
# @Project : pythonProject
# @File    : 04动作链和frame的处理.py

from selenium import webdriver
import time
#导入动作链对应的类
from selenium.webdriver import ActionChains

bro=webdriver.Chrome(executable_path=r'C:\software\Anaconda3\Scripts\chromedriver.exe')
bro.get('https://m.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果定位的标签是存在于iframe标签之中的则必须通过如下操作进行标签定位
#切换浏览器标签定位的作用域
#否则默认最外层的作用域中
bro.switch_to.frame('iframeResult')
div=bro.find_element_by_id('draggable')
#动作链
action=ActionChains(bro)
action.click_and_hold(div)
for i in range(5):
    #perform()表示立即执行动作链操作
    #move_by_offset(x,y)x水平方向,y竖直方向
    action.move_by_offset(17,0).perform()
    time.sleep(0.3)
#释放动作链
action.release()

time.sleep(10)
bro.quit()
