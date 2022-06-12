# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 10:56
# @Author  : lys
# @Project : pythonProject
# @File    : 01古诗文网验证码识别.py
import requests
from lxml import etree
from image_translate import *
if __name__ == '__main__':
    url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response=requests.get(url=url,headers=headers)
    page_text=response.text
    #parser=etree.HTMLParser(encoding='utf-8')
    #r=etree.HTML(page_text,parser=parser)
    r = etree.HTML(page_text)
    pag=r.xpath('//*[@id="imgCode"]/@src')[0]
    page_url='https://so.gushiwen.cn'+pag
    #print(page_url)
    response_img=requests.get(url=page_url,headers=headers)
    page_img=response_img.content
    #print(page_img)
    with open('./gushiwen.png','wb') as f:
        f.write(page_img)
    demo_eng('./gushiwen.png')