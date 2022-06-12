# -*- coding: utf-8 -*-
# @Time    : 2022/4/27 14:14
# @Author  : lys
# @Project : pythonProject
# @File    : c08_pandas缺失值处理.py
'''
Pandas使用这些函数处理缺失值:
1.isnull和notnull:检查是否是空值,可用于df和series
2.dropna:丢弃,删除缺失值
    2.1 axis:删除行还是列,{0 or 'index',1 or 'columns'},default 0
    2.2 how:如果等于any则任何值为空都删除,如果等于all则所有值都为空才删除
    2.3 inplace:如果为True则修改当前df,否则返回新的df
3.fillna填充空值
 3.1 value:用于填充的值,可以是单个值,或者字典(key是列名,value是值)
 3.2 method:等于ffill使用前一个不为空的值填充forword fill;等于bill使用后一个不为空的值填充backword fill
 3.3 axis:按行还是列填充,{0 or 'index',1 or 'columns'} index代表行,columns 代表列
 3.4 inplace:如果为TRUE则修改当前df .否则返回新的df
'''

#特殊excel的读取,清晰,处理
#步骤1:读取excel的时候,忽略前几个空行
import pandas as pd
fpath=r'C:\job\learning\pythonProject\venv\learn\Pandas\file\student.xlsx'
studf=pd.read_excel(fpath,skiprows=2)
#print(studf)
#步骤二 :检测空值
res=studf.isnull()
res=studf['分数'].isnull()
res=studf['分数'].notnull()
#筛选没有空分数的所有行
res=studf.loc[studf['分数'].notnull(),:]
#步骤3:删除掉全是空值的列,(删掉的是文件的第一列,因为第一列全是空值)
studf.dropna(axis='columns',how='all',inplace=True)
#步骤4:删掉全是空值的行
studf.dropna(axis='index',how='all',inplace=True)
#步骤5:将分数列为空的填充为0分
studf.fillna({'分数':0})     #不知道是不是版本问题,并不能将nan替换成0
studf.loc[:,'分数']=studf['分数'].fillna(0)  #等同于
#步骤6:将姓名的缺失值填充
#使用前面的有效值填充用ffill:forword fill
studf.loc[:,'姓名']=studf['姓名'].fillna(method='ffill')
print(studf)
#步骤7将清洗好的excel 保存
studf.to_excel(r'C:\job\learning\pythonProject\venv\learn\Pandas\file\student_clean.xlsx',index=False)
