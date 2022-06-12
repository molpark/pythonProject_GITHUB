# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 10:30
# @Author  : lys
# @Project : pythonProject
# @File    : c05_数据查询.py
'''
pandas查询数据的几种方法
1.df.loc 方法,根据行,列的标签值查询 (最最常用)
2.df.iloc 方法,更加行列的数字位置查询 用的不是很多
3.df.where 方法
4.df.query 方法

.loc方法 既能查询,又能覆盖写入,强烈推荐

pandas使用df.loc查询数据的方法
1.使用单个lable值查询数据
2.使用值列表批量查询
3.使用数值区间进行范围查询
4.使用条件表达式查询
5.调用函数查询

注意:
以上查询方法,既适用于行,也适用于列(datafram和series 都适合用这些方法查询)
注意观察降维 dataframe>series>值
'''

import pandas as pd
df =pd.read_csv(r'C:\job\learning\pythonProject\venv\learn\Pandas\file\tmp_inv_age_stock_log_202202161734.csv')
#print(df.head())
#需要注意的是字符串中全为数字,该元素也为数字类型
#设定索引为日期,方便按日期筛选,那么inbound_day 这个字段就代替了默认的0,1,2,3这样的索引,并且inbound_day成为index
#后续不会重复出现在表格中,一般最好不要轻易设置索引
df.set_index('inbound_day',inplace=True)
#查看时间序列
#print(df.index)
#print(df.head())
#替换扬基天猫超市 为扬基天猫
#如果是字符串替换成其他类型的话df.loc[:,'shop_nm']=df['shop_nm'].str.replace('超市','').astype('int32')
df.loc[:,'shop_nm']=df['shop_nm'].str.replace('超市','')   # : 代表筛选出所有行,'shop_nm' 筛选出这一列
#print(df.dtypes)
#print(df.head())

#1.使用单个label值查询数据
#行或者列,都可以传入单个值,实现精准匹配
#需要注意的是前面传去的参数的是索引,并且要关注索引的类型 查看方式print(df.dtypes)
#loc 里面第一个参数限制的是行(是对索引做限制),后一个参数限制的是列
#得到单个值 (index=20190325这一行shop_nm对应的这个值)
res=df.loc[20190325,'shop_nm']
#print(res)
#得到一个series,注意如果传进去的索引并不存在,会报错
res=df.loc[20190325,['shop_nm','product_nm']]
#print(res)

#2.使用值列表批量查询
#得到series (多行单列数据)
res=df.loc[[20181205,20181205,20181016],'shop_nm']
#print(res)
#得到dataframe (多行多列数据)
res=df.loc[[20181205,20181205,20181016],['shop_nm','inv_sort_id','sku_name']]
#print(res)

#3.使用数值区间进行范围查询
#注意行index 按区间
#发现规律有1.查看时从第一次发现20190116开始往下找直到发现20190118 如果没有就跳空.如果20190117 出现在20190116之前则无法获取
#2.索引不能是重复值,要找这种方法查找区间数据,必须要保证索引开始和结束为唯一值,不然报错
res=df.loc[20190116:20190118,'shop_nm']
#print(res)
#列index按区间,后面那个范围参数必须按照顺序从前到后,否则无结果生成,不报错
res=df.loc[20190116,'shop_info_id':'product_cd']
#print(res)

#行列都按区间查询
res=df.loc[20190116:20190118,'shop_info_id':'product_cd']
#print(res)


#4.使用条件表达式查询
#bool列表的长度得等于行数或者列数
#查询inv_sort_id 的值小于5的行列表数据   :  表示列取全部   :5 表示看前五列
#返回的是inv_sort_id比对后为true 的列表
res=df.loc[df['inv_sort_id']<5,:]
#print(res)
#复杂查询 多个限制条件,可以更换限制的字段,和限制数量记得限制条件用()分割限制条件用&
res=df.loc[(df['inv_sort_id']<5) & (df['inv_sort_id']>3),:]
res=df.loc[(df['inv_sort_id']<5) & (df['inv_sort_id']>3) & (df['shop_nm']=='扬基天猫'),:]
#print(res)



#5 直接写lambda表达式
res=df.loc[lambda df:(df['inv_sort_id']<5)&(df['inv_sort_id']>3),:]
#print(res)




res=df.loc[20181203:]
#print(res)

'''(没有实验成功,报错)
#编写自己的函数,查询2018年的数据,并且inv_sort_id <5  
def query_my_data(df):
    return  df.index.astype(str).startswith("2018") & df['inv_sort_id']<5

#print(df.loc[query_my_data, :])
#print(type(df.index))
df['biaozhi'] = df['inbound_day'].astype(str).map(lambda x : 'true' if x[0:4] == '2018' else 'False')
data = df[df.biaozhi == 'true']
print(data)
#print(data['inbound_day'])
'''