import numpy as np
n=np.array([4,5,'6'])
print(n)
m=np.array([1,2,3])
print(m)
#注意点是array方法中值的类型会统一

##创建数组
# numpy经常和数组打交道,因此首先第一步是要学会创建数组
# 在numpy中的数组的数据类型叫做ndarray,以下是两种创建的方式
#1.根据python 中的列表生成
a=[12,34,56]
a1=np.array(a)
print(a1)
print(type(a1))

#2.使用np.arrange生成,np.arrange类似于python中的range
a2=range(1,10,2)
for i in a2:
    print(i)
#此处np.arange函数中意思是start,end,step
#和上面range的含义一致
a2=np.arange(2,21,2)
print(a2)
print(type(a2))
#和range一样也可以这种方式代表0-21间隔1
a2=np.arange(21)
print(a2)

#help(np.array)

#特殊数组
#里面都是float类型
#生成一个所有元素都是0的2行2列的数组
d1=np.zeros((2,2))
print(d1)
#生成一个所有原色都是1的三行2列数组
d2=np.ones((3,2))
print(d2)
#生成一个所有元素都是8的2行2列数组
d3=np.full((2,2),8)
print(d3)
#生成一个在斜方形上元素为1,其他元素都为0的3*3的矩阵
d4=np.eye(3)
print(d4)