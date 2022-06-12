# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 17:53
# @Author  : lys
# @Project : pythonProject
# @File    : c06_pandas新增数据列.py

import pandas as pd
df=pd.read_csv(r'C:\job\learning\pythonProject\venv\learn\Pandas\file\tmp_inv_age_stock_log_202202161734.csv')
#print(df.head())
'''
在进行数据分析时,经常需要按照一定条件创建新的数据列,然后进行进一步的分析
1.直接赋值
2.df.apply方法
3.df.assign方法
4.按条件选择分组分别赋值
'''

#1,直接赋值
#替换str 类型的数据 (纯数字的字符串好像不行)
df.loc[:,'product_cd']=df['product_cd'].str.replace('YANKE0','').astype('int32')
#print(df['product_cd'])

#新增一列 如果df有两列都是数字型,可以进行加减法运算
df.loc[:,'shabi']=df['product_cd']
#print(df['shabi'])

#2.df.apply
def get_data_type(df):
    if df['inv_sort_id']>3:
        return '大'
    else:
        return '小'
#注意需要设置axis=1
df.loc[:,'data_type']=df.apply(get_data_type,axis=1)
#print(df[['inv_sort_id','data_type']])
#查看类型的计数.value_counts()
#print(df['data_type'].value_counts())

#3.df.assign 方法 新添加的inv_sort_id_new 会出现在新的df_new对象 中的最后一列
df_new=df.assign(
inv_sort_id_new=lambda x:x['inv_sort_id']*10
)
#print(df_new.head())

#4.按条件选择分组分别赋值
#按条件先选择数据,然后对这部分数据赋值新列
#先创建空列(这是第一张创建新列的方法)
df['wencha_type']=''
df.loc[df['inv_sort_id']>3,'wencha_type']='温差大'
df.loc[df['inv_sort_id']<=3,'wencha_type']='温差小'
print(df['wencha_type'])
print(df['wencha_type'].value_counts())