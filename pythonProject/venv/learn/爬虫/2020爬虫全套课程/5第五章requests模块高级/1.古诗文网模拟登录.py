# -*- coding: utf-8 -*-
# @Time    : 2022/5/8 20:54
# @Author  : lys
# @Project : pythonProject
# @File    : 1.古诗文网模拟登录.py
import sys

import requests
from lxml import etree
from hm_message import image_translate

#　1、实例化session对象
#用session 使登录状态不丢
session = requests.session()
url_get ='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
url_post='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
url_detail='https://so.gushiwen.cn/user/collect.aspx?type=s&id=2749237&sort=t'
cookie='''Hm_lvt_9007fab6814e892d3020a64454da5a55=1651763893,1651821335,1651892213,1651977804; ticketStr=202007475%7cgQH27zwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyekZhQlIxbGVkN2kxQVZkdk55MVgAAgQ5wHdiAwQAjScA; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1652015173; codeyzgswso=41da140f70048126login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1651763893,1651821335,1651892213,1651977804; ASP.NET_SessionId=eowfi5cl0hvet05sfanx213j; login=flase; ticketStr=202007475%7cgQH27zwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyekZhQlIxbGVkN2kxQVZkdk55MVgAAgQ5wHdiAwQAjScA; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1652015173; codeyzgswso=41da140f70048126'''
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

#登录前准备验证码
def deng_ex():
    response=session.get(url=url_get,headers=headers)
    page_text=response.text
    parser=etree.HTMLParser(encoding='utf-8')
    r=etree.HTML(page_text,parser=parser)
    img_path=r.xpath('//*[@id="imgCode"]/@src')[0]
    img_path='https://so.gushiwen.cn'+img_path
    response = session.get(url=img_path, headers=headers)
    pic_text=response.content
    with open('gswyanzhengma.png','wb') as f:
        f.write(pic_text)
    image_value=image_translate.demo_eng('gswyanzhengma.png')
    print(image_value)
    return image_value

#拿验证码,账号密码登录后获取页面返回值
def deng_ed():
    image_value = deng_ex()
    data = {
        'from': 'http: // so.gushiwen.cn / user / collect.aspx',
        'email': '13818106451',
        'pwd': 'Lu61241025',
        'code': image_value.replace('\n',''),
        'denglu': '登录'
    }
    print(data)
    response=session.post(url=url_post,headers=headers,data=data)
    status=response.status_code
    if status==200:
        print(status)
    else:
        print(status)
        print('响应失败')

    page_text=response.text
    with open('gushi.html','w',encoding='utf-8') as f:
        f.write(page_text)

#查看登录页面详细信息
def deng_detail_ed():
    #headers中增加cookie是在本地记录cookie(cookie一般有有效期)
    #增加使用cookie在请求头的实验
    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    #     "cookie":"login=flase; ticketStr=202007475%7cgQH27zwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyekZhQlIxbGVkN2kxQVZkdk55MVgAAgQ5wHdiAwQAjScA; gsw2017user=2749237%7cE8345910174EE18E21BF106C7AB721C2; login=flase; wxopenid=defoaltid; gswZhanghao=13818106451; gswPhone=13818106451; Hm_lvt_9007fab6814e892d3020a64454da5a55=1651821335,1651892213,1651977804,1652151652; ASP.NET_SessionId=w4d54v4lwr1kv4svj2v4oxwe; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1652151744"
    # }
    # response=requests.get(url=url_detail,headers=headers)

    #session是让服务器记录cookie (建议使用此种方法)
    response=session.get(url=url_detail,headers=headers)
    page_text=response.text
    with open('./gs_detail.html','w',encoding='utf-8') as f:
        f.write(page_text)


def main():
    deng_ed()
    deng_detail_ed()

if __name__ == '__main__':
    main()

#P35 模拟登录cookie