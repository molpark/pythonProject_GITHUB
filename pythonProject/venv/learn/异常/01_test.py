# -*- coding: utf-8 -*-
# @Time    : 2022/5/15 16:49
# @Author  : lys
# @Project : pythonProject
# @File    : 01_test.py

# value=8/0
# print(value)
import time
import traceback
'''
总结 
有try except 返回值为0程序不会报错
有如果有raise 异常返回值是1 报错推出

try raise  except 中 raise 其实没有啥意义.抛出的异常会被下面的except 捕获
'''



n=0
try:
    if n==0:
        pass
        #raise Exception('被除数不能为0')
    value = 8 / n
    print(value)
# except Exception as e:
#     print(e)
# except:
#     info=traceback.format_exc()
#     print(info)
#没有异常会执行else 的代码
# else:
#     print('no error')
#不管有没有异常都会执行
finally:
    print('结束')

# a=0
# if a==0:
#     raise Exception('被除数a不能为0')


import pandas as pd
pd.data




'asdsadsad'

