import pandas as pd
import numpy as np

#Series
#是一种类似于一维数组的对象,它由一组数据(不同数据类型)
#以及一组与之相关的数据标签(即索引)组成
#1.1仅有数据列表即可产生最简单的Series
sl=pd.Series([1,'a',56,'vb5'])
#sl=pd.Series([1,'a',56,'vb5']).index('w','x','y','z') 也可以单独指定索引名称,默认是从0开始
#左侧为索引,右侧是数据
#print(sl)
#获取索引
#print(sl.index)
#获取数据
#print(sl.values)
#类似于list可以循环获取倒
# for i in sl.values:
#     print(i)

#使用字典创建Series
sdata={'aaa':5,'bbb':6,'ccc':7}
s3=pd.Series(sdata)
#print(s3)
# #索引也可以循环获取到
# print(s3.index)  ##索引就是字典的key
# for i in s3.index:
#     print(i)
#可以当作字典来根据key 获取数据 当获取一个值的时候返回的是该值的真实类型比如数字,字符等
# print(s3.get('aaa'))
# print(s3['aaa'])
#获取多个值 返回的是series类型
#print(s3[['aaa','bbb']])

