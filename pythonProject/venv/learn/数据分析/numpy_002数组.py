#可以打印数组中的值的类型
import numpy as np
a=np.arange(10)
print(a)
#可以打印数组中的值的类型
print(a.dtype)
#对数组中的数组赋类型,可以转成float,也可以int32转成int8
b=np.array([1,2,3,4,5,],dtype=np.int8)
print(b)
print(b.dtype)

##object类型
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
d=np.array([Person('小A',89),Person('小B',22)])
print(d)
print(d.dtype)
#测试语句
d=Person('小王',12)
print(d.name)

#字符串类型
e=np.array(['1','2',],dtype='string_')
e=np.array(['1','2',],dtype='S')
print(e)
print(e.dtype)

#数组的类型转换
f=e.astype('int8')
print(f)
print(f.dtype)
