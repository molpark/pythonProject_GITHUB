# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 23:00
# @Author  : lys
# @Project : pythonProject
# @File    : 4.bs4案例.py
#需求:爬取三国演义小说所有的章节标题和章节内容

import requests
from bs4 import BeautifulSoup
import os
if __name__ == '__main__':
    url='https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response=requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    sanguo_data=response.text
    sg_soup=BeautifulSoup(sanguo_data,'lxml')
    mulu_list=[]
    line = 0
    while True:
        try:
            res=sg_soup.select('.book-mulu>ul a')[line].get_text()
            mulu_list.append(res)
            line+=1
        except Exception as e:
            print(e)
            break
    #print(mulu_list)
    if os.path.exists('./sanguo.txt'):
        os.remove('./sanguo.txt')
    with open('./sanguo.txt', 'w', encoding='utf-8') as f:
        for i in range(1,len(mulu_list)):
            bt_line=i-1
            i=str(i)
            n_url=f'https://www.shicimingju.com/book/sanguoyanyi/{i}.html'
            n_response=requests.get(url=n_url,headers=headers)
            n_response.encoding = 'utf-8'
            yy_data=n_response.text
            yy_soup=BeautifulSoup(yy_data,'lxml')
            chapter_content=[]
            res=yy_soup.find('div',class_='chapter_content').get_text()
            f.write(mulu_list[bt_line])
            f.write('\n')
            f.write(res)

#p23 8 xpath解析


