# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 21:26
# @Author  : lys
# @Project : pythonProject
# @File    : testbs4.py

'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是python对象,所有对象可以归纳唯四种
--Tag
--NavigableString
--BeautifulSoup
--Comment
'''

#一般需要用到的包
from bs4 import BeautifulSoup    ##网页解析获取数据
import re                        ##正则表达式 进行文字匹配
import urllib.request,urllib.error,urllib.parse  ##指定url,获取网页数据
import xlwt                         ##进行excel操作
import sqlite3                      ##进行SQLite数据库操作


with open("./baidu.html",'rb') as f:
    html=f.read().decode('utf-8')
bs=BeautifulSoup(html,'html.parser')
#print(type(bs))  #<class 'bs4.BeautifulSoup'>

#找到的第一个标签及其内容
#print(bs.title)
#print(bs.a)
#print(type(bs.head)) #<class 'bs4.element.Tag'>
#1.Tag 标签及其内容:只能拿到第一个标签及其内容
# print(bs.title)
# #2.NavigableString  标签里的内容(这块用的比较多)(字符串)
# print(bs.title.string)  #就只要里面的内容
# print(type(bs.title.string))#<class 'bs4.element.NavigableString'>

#快速找到一个标签里面的属性,保存方式是字典
# print(bs.a.attrs)
# print(type(bs.a.attrs))#<class 'dict'>


#3.BeautifulSoup 表示整个文档
# print(type(bs))
# print(bs.name)
# print(bs.attrs)

#4.Comment 注释 ,是一个特殊的NavigableString ,输出的内容不好含注释符号
#这里B并没有拿到注释数据
# print(bs.b)
# print(bs.b.string)
# print(type(bs.b.string))

#############################
#文档的遍历
#遍历文档树

#1.contents:获取tag的所有子节点,返回一个list
#print(bs.head.contents)
#用列表索引来获取他的某一个元素
#print(bs.head.contents[1])
#2.children :获取Tag的所有子节点,返回一个生成器
# for child in bs.body.children:
#     print(child)
#3.descendants:获取tag 的所有子孙节点
#4.strings:如果tag包含多个字符串,即在子孙节点中有内容,可以用此获取,而后进行遍历
#5 stripped_string:与strings用法一致,只不过可以去除掉那些多余的空白内容
#6 parent:获取tag的父节点
#7 parents:递归得到父辈元素的所有节点,返回一个生成器
#8 preious_sibling:获取当前tag的上一个节点,属性通常是字符串或空白,真实结果是当前标签与上一个标签
#之间的顿号和换行符
#9 next_sibling:获取当前tag的下一个节点,属性通常是字符串或空白,真是结果是当前标签与下一个标签之间的顿号与
#换行符
#10 previouus_siblings:获取当前tag 的上面所有的兄弟节点,返回一个生成器
#11 next_siblings:获取当前tag的下面所有的兄弟节点,返回一个生成器
#12 previous_element:获取解析过程中上一个被解析的对象(字符串or tag),可能与previous_sibling相同,
#但通常是不一样的
#13 next_element:获取解析过程中下一个被解析的对象(字符串或tag),可能与next_sibling相同.但通常是不一样的阿
#14 previous_elements:返回一个生成器,可以向前访问文档的解析内容
#15 next_elements:返回一个生成器,可以向后访问文档的解析内容
#16 has_attr:判断tag是否包含属性






#文档的搜索




