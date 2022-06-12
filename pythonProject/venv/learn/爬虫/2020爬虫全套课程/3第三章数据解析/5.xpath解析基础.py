# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 10:10
# @Author  : lys
# @Project : pythonProject
# @File    : 5.xpath.py

from lxml import etree
if __name__ == '__main__':
    #实例化好了一个etree对象,且将被解析的源码加载到了该对象中
    parser = etree.HTMLParser(encoding='utf-8')
    tree=etree.parse('./sogou.html',parser=parser)
    #r=tree.xpath('/html/body/div/div/div/ul/li/span')
    #r=tree.xpath('/html//div')
    #r = tree.xpath('//div')
    #r=tree.xpath('//div[@class="top-nav"]')
    # r=tree.xpath('//div[@class="top-nav"]/ul/li[2]/a')  #索引从1开始的
    # r = tree.xpath('//div[@class="top-nav"]/ul/li[2]/a/text()')[0]  #返回的是列表再取第一个元素
    #r = tree.xpath('//div[@class="top-nav"]/ul/li/a/text()')#返回的是列表
    # r=tree.xpath('//li[2]//text()') #直接定位li标签
    #r=tree.xpath('//div[@class="top-nav"]//text()') #获取的是标签中非直系的文本内容
    r = tree.xpath('//div[@class="top-nav"]//a/@href') #获取a下的属性值
    print(r)