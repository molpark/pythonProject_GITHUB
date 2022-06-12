# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 12:29
# @Author  : lys
# @Project : pythonProject
# @File    : 7.xpath解析案例-4k图片解析爬取.py
import os.path

import requests
from lxml import etree
if __name__ == '__main__':
    pth='./pic'
    if not os.path.exists(pth):
        os.mkdir(pth)
    url='https://pic.netbian.com/4kmeinv/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response=requests.get(url=url,headers=headers)
    #可以手动设定响应数据的编码格式
    #response.encoding='utf-8'
    page_text=response.text
    parser=etree.HTMLParser(encoding='utf-8')
    tree=etree.HTML(page_text,parser=parser)
    r=tree.xpath('//*[@id="main"]/div[3]/ul')
    for i in r:
        cif=i.xpath('./li/a/img/@src')
        name = i.xpath('./li/a/img/@alt')
        for ic in name:
            #通用处理中文乱码的解决方案,这个和上面response.encoding('utf-8')在这个案例的时候有冲突
            #一般还是在中文这边单独做个处理
            name_ic =ic.encode('iso-8859-1').decode('gbk')
            print(name_ic)
        for op in cif:
            cif_n=op.split('/')[-1]
            pic_path = pth+'/'+ cif_n
            cif_tt='https://pic.netbian.com'+op
            with open(pic_path,'wb') as f:
                response=requests.get(url=cif_tt,headers=headers)
                pic=response.content
                f.write(pic)

