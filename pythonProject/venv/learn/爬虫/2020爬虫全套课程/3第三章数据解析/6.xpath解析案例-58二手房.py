# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 11:39
# @Author  : lys
# @Project : pythonProject
# @File    : 6.xpath解析案例-58二手房.py
from lxml import etree
import requests
if __name__ == '__main__':
    #爬取页面源码数据
    url='https://sh.58.com/ershoufang/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response=requests.get(url=url,headers=headers)
    page_text=response.text
    #print(page_text)
    # 现在58必须要登录,现在返回的是需要验证码的页面
    parser=etree.HTMLParser(encoding='utf-8')
    tree=etree.HTML(page_text,parser=parser)
    r=tree.xpath('//div[@id="dlg-toolbar"]//label/text()')
    #r = tree.xpath('./div[@id="dlg-toolbar"]//label/text()')#./和文件一样意思当前目录下的
    print(r)
