import pandas as pd
import matplotlib.pyplot as plt
#使用pd.read_csv读取文件
fpath=r'C:\job\learning\pythonProject\venv\learn\Pandas\file\tmp_inv_age_stock_log_202202161734.csv'
n=pd.read_csv(fpath)


#查看前几行数据 默认读五行
#print(n.head())
#print(n.head(2))

#查看数据的形状，返回(行数，列数)
#print(n.shape)
#查看列名列表
#print(n.columns)
#查看索引列
#print(n.index)
#查看每列的数据类型
#print(n.dtypes)

#指定分隔符读取
n=pd.read_csv(fpath,sep=';')
#print(n.head())

'''
将列分隔符改成 ; 
将编码改为 latin1 （默认为 utf-8 ） 
解析 Date 列中的日期 
告诉它我们的日期将日放在前面，而不是月 
将索引设置为 Date 
fixed_df = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date') fixed_df[:3]
'''


#展示成图表
#plt.plot(n['inbound_day'])
#plt.show()

#选择一列读取
#print(n['company_name'])

#读取excel 文件
fpath=r'C:\job\learning\pythonProject\venv\learn\Pandas\file\student.xlsx'
studf=pd.read_excel(fpath,skiprows=2) #忽略前两行