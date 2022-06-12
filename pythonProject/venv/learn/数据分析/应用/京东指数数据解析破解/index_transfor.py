# *_* coding:utf-8 *_*
# Author:ZhengYuan

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# matplotlib绘图中文显示
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# df = pd.read_excel('../data/JD数据最新20220323.xlsx', sheet_name='成交金额data')
df = pd.read_excel('./JD数据最新20220408.xlsx', sheet_name='成交金额data')
# df = df[df['全店成交金额指数'] >= 2000000]
# df = df[['店铺名称', '二级行业名称', '全店成交金额指数', '成交金额']]
# df.dropna(inplace=True)
# print(df['二级行业名称'].unique())
# df = df[(df['二级行业名称'] == '运动鞋包') | (df['二级行业名称'] == '时尚女鞋')]
# print(df['全店成交金额指数'].value_counts(bins=[0, 10000000, 20000000, 30000000, 50000000,
#                                         60000000, 70000000]))
df = df[(df['全店成交金额指数'] >= 30000000) & (df['全店成交金额指数'] < 50000000)]
df.sort_values(by=['全店成交金额指数'], inplace=True)
print(df)
print('df长度：', len(df))
df.rename(columns={'全店成交金额指数': 'index', '成交金额': 'num'}, inplace=True)
print(df.isnull().any())
x = df['index']
y = df['num']
plt.title('交易')
plt.xlabel('全店成交金额指数')
plt.ylabel('成交金额')
plt.scatter(x, y)
plt.savefig('./scatter.png')
#plt.show()
print('1111111111111111')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=2020)
print('22222222222222222')
fit_para = np.polyfit(x_train, y_train, 5)
print('3333333333333')
y_fun = np.poly1d(fit_para)
print(y_fun)
print(fit_para)

# y_test_hat = np.polyval(fit_para, x_test)

y_test_hat = y_fun(x_test)
x_test = pd.DataFrame(x_test)
y_test = pd.DataFrame(y_test)
y_test_hat = pd.DataFrame(y_test_hat, columns=['pred_num'])
x_test = x_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)
df_result = x_test.join(y_test)
df_result = df_result.join(y_test_hat)
print(df_result)
print(df_result.dtypes)
plt.plot(df_result['index'], df_result['num'], 'o', color='r')
plt.plot(df_result['index'], df_result['pred_num'], '*', color='g')
plt.savefig('./true_pred')
plt.show()

df_result.to_excel('./pred.xls', index=False)

r2 = r2_score(y_test, y_fun(x_test))
print('r2:', r2)

mse = mean_squared_error(y_test, y_fun(x_test))
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_fun(x_test))
# mape = abs((true_value-pre_value)/true_value).mean()
# mape = mean_absolute_error((y_test - y_fun(x_test)) / y_test, np.zeros(y_test.shape))
print('rmse:', rmse)
print('mae:', mae)
# print('mape:', mape)