# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 20:37
# @Author  : lys
# @Project : pythonProject
# @File    : teste01.py




from urllib.request import urlopen
import re
p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('https://www.baidu.com').read().decode()
for url, name in p.findall(text):
 print('{} ({})'.format(name, url))