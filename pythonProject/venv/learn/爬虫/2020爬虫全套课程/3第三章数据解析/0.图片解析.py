# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 15:35
# @Author  : lys
# @Project : pythonProject
# @File    : 1.正则解析.py
#需求:爬取糗事百科中糗图板块下所有的糗图图片
import requests
if __name__ == '__main__':
    #如何爬取图片数据
    url='https://n.sinaimg.cn/spider20220504/107/w1024h683/20220504/cf50-caf51eafc13ec42a18050657b0216099.png'
    #content返回的是二进制形式的图片数据
    #text(字符串) content(二进制) json()(json对象)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response=requests.get(url,headers=headers)
    image=response.content
    with open('./baidu.jpg','wb') as f:
        f.write(image)
