import pandas as pd
import numpy as np

##DataFrame
'''
DataFrame是一个表格型的数据结构
每列可以是不同的值类型(数值,字符串,布尔值等)
既有行索引index,又有列索引colums
可以被看作由Series组成的字典
创建dataframe 最常用的方法,类似与读取文本文件,excel,mysql数据库
'''

data={
 'state':['oho','aba','csc']
 ,'year':[2000,2001,2002]
,'pop':[1.2,3.3,5.2]
 }
dataf=pd.DataFrame(data)
#print(dataf)
#查询多列,
#print(dataf['state'])
#print(dataf[['state','year']])

#查询行,查询索引 (行代表的就是表头,字典中的key)
#print(dataf.columns)
#print(dataf.index)




#从dataframe中查询出Series
'''
如果只查询一行,一列,那么返回的是pd.series
如果查询多行,多列,那么返回的是pd.DataFrame
'''

#列
# print(dataf['state'])
# print(type(dataf['state'])) #series
# print(type(dataf[['state','year']]))#DataFrame

#行
#loc 列表的切片元素
#查询数据一行,结果是Series
print(dataf.loc[1]) #从0开始代表了第一行   #类型是series
#查询多行,结果是DataFrame
print(dataf.loc[0:1]) #类型是dataframe 包含末尾模式