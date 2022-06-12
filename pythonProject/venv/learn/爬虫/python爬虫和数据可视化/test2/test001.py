# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 19:48
# @Author  : lys
# @Project : pythonProject
# @File    : test001.py
from subprocess import Popen, PIPE
text = open('baidu.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
tidy.stdin.write(text.encode())
tidy.stdin.close()
print(tidy.stdout.read().decode())