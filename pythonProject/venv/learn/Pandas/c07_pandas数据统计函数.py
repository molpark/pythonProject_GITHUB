# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 22:30
# @Author  : lys
# @Project : pythonProject
# @File    : c07_pandas数据统计函数.py
'''
1.汇总类统计
2.唯一去重和按值计算
3.相关系数和协方差
'''

import pandas as pd

fpath=r'C:\job\learning\pythonProject\venv\learn\Pandas\file\tmp_inv_age_stock_log_202202161734.csv'
df=pd.read_csv(fpath)

#1.汇总类统计(针对的都是数字类型的统计)
#一下子提取所有数字列统计结果
res=df.describe()
#查看单个Series的数据 以下大部分计算方法都适用
res=df['inv_sort_id'].mean
#查看单个series最大值
res=df['inv_sort_id'].max()
#查看单个series最小值
res=df['inv_sort_id'].min()
#查看单个series的汇总值
res=df['shop_info_id'].sum()
#print(res)


#2.唯一去重和按值计算
#2.1唯一性去重
#一般不用于数值列,而是枚举,分类列
#查看单个series(字符串类型)的枚举值(会对productnm中的值进行去重后展示)
res=df['product_nm'].unique()
#2.2按值计数 (计算productnm每个值对应一共有多少个,并且会根据count出来的结果正序排序)
res=df['product_nm'].value_counts()
#print(res)

#相关系数和协方差
'''
用途(超级厉害):
1.两只股票是不是同涨同跌?程度多大?正相关还是负相关?
2.产品的销量的波动,跟哪些因素正相关,负相关,程度有多大?
来自知乎,对于两个变量X,Y:
1.协方差:衡量同向反向程度,如果协方差为正,说明X,Y同向变化,协方差越大说明同向程度越高;
如果协方差为负,说明X,Y反向运动,协方差越小说明反向程度越高
2.相关系数:衡量相似度程度,当他们的相关系数为1时,说明两个变量变化时的正向相似度最大,当相关系数为-1时
说明两个变量变化的反向相似度最大
'''
#协方差矩阵:
res=df.cov()
#相关系数矩阵
res=df.corr()
#单独查看inboundday 和 qty 的相关系数
res=df['inbound_day'].corr(df['qty'])

print(res)