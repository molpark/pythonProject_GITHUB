# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 23:08
# @Author  : lys
# @Project : pythonProject
# @File    : sys_001标准库.py

import sys
print(sys.version)#版本号
print(sys.maxsize)#能够表示的最大的int
print(sys.path)
print(sys.platform) #平台
print(sys.copyright) #版权
print(sys.argv)  #参数返回的是一个列表
#print(sys.argv[0])  #参数
#print(sys.argv[1])
#sys.exit(1)
print(sys.getdefaultencoding()) #获取编码格式
print(sys.getfilesystemencoding()) #获取文件的编码格式
print(sys.getrecursionlimit()) #最大递归次数
sys.setrecursionlimit(100) #修改递归次数限制
print(sys.getrecursionlimit()) #最大递归次数
def rec(i):
    print(i)
    rec(i+1)
rec(1) #会抛出递归异常