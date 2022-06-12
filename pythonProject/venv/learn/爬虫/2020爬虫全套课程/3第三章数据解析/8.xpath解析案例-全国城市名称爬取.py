# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 14:55
# @Author  : lys
# @Project : pythonProject
# @File    : 8.xpath解析案例-全国城市名称爬取.py
#p27 12 xpath解析案例-全国城市名称爬取
#https://www.aqistudy.cn/historydata/
# import requests
# from lxml import etree
# if __name__ == '__main__':
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
#     }
#     url='https://www.aqistudy.cn/historydata/'
#     response=requests.get(url=url,headers=headers)
#     page_text=response.text
#     #print(page_text)
#     parser=etree.HTMLParser(encoding='utf-8')
#     tree=etree.HTML(page_text,parser=parser)
#     r=tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li')
#     #print(r)
#     city_page=[]
#     for i in r:
#         city_page_new=i.xpath('./a/text()')[0]
#         city_page.append(city_page_new)
#     print(city_page)
#

##热门城市和全部城市一起获取
import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    url='https://www.aqistudy.cn/historydata/'
    response=requests.get(url=url,headers=headers)
    page_text=response.text
    #print(page_text)
    parser=etree.HTMLParser(encoding='utf-8')
    tree=etree.HTML(page_text,parser=parser)
    #解析到热门城市和所有城市对应的a标签
    #热门的a标签层级关系div/ul/li/a
    #全部城市a标签的层级关系 dv//ul/div[2]/li/a
    # | 代表或
    city_names=[]
    a_list=tree.xpath('//div[@class="bottom"]/ul/li/a |//div[@class="bottom"]/ul/div[2]/li/a')
    for a in a_list:
        city_name=a.xpath('./text()')[0]
        city_names.append(city_name)
    print(city_names)
