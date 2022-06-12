# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 12:31
# @Author  : lys
# @Project : pythonProject
# @File    : 2线程池的基本使用.py

#使用线程池方式执行
#导入
#进程池
from multiprocessing import Pool as processPool
#线程池
from multiprocessing.dummy import Pool as threadPool
import time

# def get_page(str):
#     print('正在下载',str)
#     time.sleep(2)
#     print('下载成功',str)
#
# name_list=['11','22','33','44']
#
# start_time=time.time()
#
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
#
# end_time=time.time()
#
# print(f'耗时{end_time-start_time}')
#

start_time=time.time()
def get_page(str):
    print('正在下载'+str)
    time.sleep(2)
    print('下载成功'+str)

name_list=['11','22','33','44']

#实例化一个线程池对象
pool=threadPool(4)
#将列表中每一个列表元素传递给get_page进行处理
pool.map(get_page,name_list)
end_time=time.time()
print(f'耗时{end_time-start_time}')