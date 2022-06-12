# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 10:50
# @Author  : lys
# @Project : pythonProject
# @File    : re正则练习.py
import re
#提取出python
key='javapythonc++python'
res=re.findall('python',key)[0]
#提取helloworld
key='<html><h1>helloworld<h1><html>'
res=re.findall('<h1>(.*)<h1>',key)[0]
#提取170
key='我喜欢170的女生'
res=re.findall('\d+',key)[0]
#提取出http://和https://
key='http://www.baidu.com and https://bok.org'
res=re.findall('https?://',key)
#提取出hello
key='lalala<HtmL>hello</hTMl>adsdsa'
res=re.findall('<[hH][Tt][mM][Ll]>(.*)</[hH][Tt][mM][Ll]>',key)
#提取出hit.
key='bobo@hit.edu.com'
res=re.findall('h.*?\.',key)
#匹配sas和saas
key='saas and sas and saaas'
res=re.findall('sa{1,2}s',key)
print(res)
