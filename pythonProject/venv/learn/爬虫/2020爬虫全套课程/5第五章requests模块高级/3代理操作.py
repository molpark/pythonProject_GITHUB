# -*- coding: utf-8 -*-
# @Time    : 2022/5/11 22:19
# @Author  : lys
# @Project : pythonProject
# @File    : 3代理操作.py


import requests
url='https://www.baidu.com/s?wd=ip'
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
proxies={
    'http':'220.168.52.245:53548'
}
#,proxies=proxies
response=requests.get(url=url,headers=headers,proxies=proxies)
page_text=response.text
with open('./baidu_ip.html','w',encoding='utf-8') as f:
    f.write(page_text)
#反爬机制:封ip
#反反爬策略:使用代理进行请求发送