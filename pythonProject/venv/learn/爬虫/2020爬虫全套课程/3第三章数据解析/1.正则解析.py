# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 16:27
# @Author  : lys
# @Project : pythonProject
# @File    : 1.正则解析.py
import requests
import re
if __name__ == '__main__':
    url='https://slide.sports.sina.com.cn/n/slide_2_789_277737.html'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    #使用通用爬虫对url对应的一整张页面进行爬起
    response=requests.get(url=url,headers=headers)
    page_text=response.text
    #print(page_text)
    #使用聚焦爬虫将页面中所有的图进行解析/提取
    ex='<meta itemprop="image" content="http:(.*?)" />'
#<meta itemprop="image" content="http://n.sinaimg.cn/sports/2_img/dfic/cf0d0fdd/106/w1024h682/20220414/67bc-c7ccd87a50a78b84093687855b69a07e.jpg" />
    img_src_list=re.findall(ex,page_text,re.S)
    #print(img_src_list)
    for src in img_src_list:
        src='https:'+src
        #image_name=re.findall(r'20220414/(.*?).jpg',src)
        image_name =src.split('/')[-1]
        print(image_name)
        response=requests.get(url=src,headers=headers)
        image=response.content
        with open(f'./{image_name}','wb') as f:
            f.write(image)

