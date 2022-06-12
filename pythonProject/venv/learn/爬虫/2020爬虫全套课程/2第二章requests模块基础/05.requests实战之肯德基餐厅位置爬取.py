# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 22:20
# @Author  : lys
# @Project : pythonProject
# @File    : 05.requests实战之肯德基餐厅位置爬取.py
import requests
import json
if __name__ == '__main__':
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    data={
        'cname':'',
        'pid':'',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '100',
        'op': 'keyword'
    }
    response=requests.post(url=url,headers=headers,data=data)
    #虽然看了content-type为text但是实际格式还是字典的json格式.如果text拿下来也行,但是展示有问题
    page_file=response.json()
    print(page_file)
    json.dump(page_file, open('kdj.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
    print('kdj  over')

