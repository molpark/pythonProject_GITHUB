# -*- coding: utf-8 -*-
# @Time    : 2022/5/21 12:10
# @Author  : lys
# @Project : pythonProject
# @File    : 07基于selenium实现12306登录.py
#12306现在会检查selenium

from selenium import webdriver
import time
#导入动作链对应的类
from selenium.webdriver import ActionChains
#实现规避检测
from selenium.webdriver import ChromeOptions
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
from PIL import Image


#实现规避检测
option=ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
#实现无可视化界面的操作
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


bro=webdriver.Chrome(executable_path=r'C:\software\Anaconda3\Scripts\chromedriver.exe',options=option)
#浏览器窗口最大化
#bro.maximize_window()
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
username =bro.find_element_by_id('J-userName')
password=bro.find_element_by_id('J-password')
username.send_keys('13818106451')
password.send_keys('Lu61241025')
time.sleep(2)
cli_denglu=bro.find_element_by_id('J-login')
cli_denglu.click()
time.sleep(2)
huadong =bro.find_element_by_id('nc_1__scale_text')
action=ActionChains(bro)
n=300
#action.drag_and_drop_by_offset(huadong,n,0).perform()
#action.click_and_hold(huadong)
#action.move_by_offset(n,0).perform()

script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
bro.execute_script(script)
action.click_and_hold(huadong)
action.move_by_offset(n,0).perform()
#action.drag_and_drop_by_offset(huadong,n,0).perform()
time.sleep(5)
page_text=bro.page_source
print(page_text)


##在之前还是识别图片并且点击
#需要下载验证码,识别再处理
#截图
bro.save_screenshot('aa.png')
#裁剪图片
#确定验证码图片对应的左上角和右小角的坐标(裁剪的区域)
#此处需要定位到图片,现在开发时没有图片,实际实验时需要拿img测试
code_img_ele=bro.find_element_by_xpath('//*[@id="pop_16531195546704273"]/div[2]/div[1]/div')
location=code_img_ele.location #左上角的x,y
print(location)
size=code_img_ele.size  #验证码对应的长和宽
print(size)
#左上角和右下角坐标
#如果开了bro.maxmize_window()坐标位置需要放大一般1.25的备注或者2倍
range=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
#至此验证码图片区域就确定下来了
i=Image.open('./aa.png')
code_img_name='./code.png'
#crop根据指定区域进行图片裁剪
frame=i.crop(range)
frame.save(code_img_name)



bro.quit()

