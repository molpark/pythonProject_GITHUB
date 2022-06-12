import numpy as np
import time

a=[]
t1=time.time()
for i in range(1000000):
    a.append(i**2)
t2=time.time()
print(t2-t1)

t3=time.time()
#np.arange(12)出来的是一个数组
#对数组操作是对中的每一个值进行操作
#和列表的区别是列表需要循环对每一个值操作
#数组可以直接对数组对象操作
b=np.arange(1000000)**2
t4=time.time()
print(t4-t3)

c=np.arange(5)
print(c)
for i in c:
    print(i)

