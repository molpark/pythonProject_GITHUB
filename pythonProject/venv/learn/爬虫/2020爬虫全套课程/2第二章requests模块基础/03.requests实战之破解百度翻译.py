# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 20:40
# @Author  : lys
# @Project : pythonProject
# @File    : 03.requests实战之破解百度翻译.py
#需求破解百度翻译
#post请求(携带了参数)
#响应数据是一组json数据

import requests
import json
if __name__ == '__main__':
    #1.指定url
    post_url='https://fanyi.baidu.com/sug'
    #2.UA伪装:将对应的User-Agent封装到一个字典中
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    #3.post请求参数处理(同get请求一致)
    #可以在payload中查看到
    word=input('enter a word: ')
    data={
        'kw':word
    }
    #4.请求发送
    response=requests.post(url=post_url,data=data,headers=headers)
    #5.获取响应数据:json()方法返回的是obj (如果确认响应数据是json类型的才可以使用json方法)
    #查看页面headers中content-type的类型可以判断respon返回的类型
    dic_obj=response.json()
    print(dic_obj)
    #持久化存储
    #json中有中文ensure_ascii=False 阿斯克码为False,否则出来的结果是/u6559 这中形式
    json.dump(dic_obj, open('baidu_fanyi.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)

#https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A9