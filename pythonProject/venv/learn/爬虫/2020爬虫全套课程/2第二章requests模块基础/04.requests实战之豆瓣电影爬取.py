# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 21:09
# @Author  : lys
# @Project : pythonProject
# @File    : 04.requests实战之豆瓣电影爬取.py

import requests
import json
if __name__ == '__main__':
    url='https://movie.douban.com/j/chart/top_list'
    param={
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',#从库中的第几部电影去取
        'limit': '20'#一次请求取出的个数
    }
    headers= {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response=requests.get(url=url,params=param,headers=headers)
    page_list=response.json()
    print(type(page_list))
    json.dump(page_list, open('douban.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)


