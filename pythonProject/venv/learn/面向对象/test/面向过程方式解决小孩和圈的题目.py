# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 15:18
# @Author  : lys
# @Project : pythonProject
# @File    : 面向过程方式解决小孩和圈的题目.py

# list_cycle=[]
# cycle=range(1,501)
# for i in cycle:
#     list_cycle.append(i)
# print(list_cycle)

#推导式
cycle=[x for x in range(1,501)]
step=1
while len(cycle)>1:
    dels=[]
    for kid in cycle:
      if step %3==0:
        dels.append(kid)
      step+=1
    # for kid in dels:
    #     cycle.remove(kid)
    #推导式
    cycle=[i for i in cycle if i not in dels]
print(cycle)
