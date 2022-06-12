# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 19:22
# @Author  : lys
# @Project : pythonProject
# @File    : 02.requests实战之网页采集器.py
'''
UA:USER-AGENT 请求载体的身份标识
UA检测:门户网站的服务器会检测对应请求的载体身份标识,如果检测到请求的载体身份标识为某一款浏览器
说明该请求是一个正常的请求,但是,如果检测到请求的载体身份标识不是一款浏览器,
则表示为不正常的请求(爬虫),则服务器端很有可能拒绝该次请求
UA伪装:让爬虫对应的请求载体身份表示伪装成某一款浏览器
'''
import requests
if __name__ == '__main__':
    url='https://www.sogou.com/web'
    #处理url携带的参数:封装到字典中
    kw=input('enter a word: ')
    # UA伪装:将对应的User-Agent封装到一个字典中
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
             }
    param={
        "query":kw
    }
    #对指定的url发起的请求对应的url是携带参数的,并且请求过程中处理了参数
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as f:
        f.write(page_text)
    print(fileName,'保存成功')
#https://fanyi.baidu.com/?aldtype=16047#auto/zh