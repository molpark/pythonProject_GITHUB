import numpy as np

#这个就只是最普通的随机数,返回的是一个0-1之间的随机数
a=np.random.random()
print(a)
print(type(a))
#随机数组
#随机出来的是包含两个float类型值的数组
b=np.random.random(2)
print(b)
print(type(b))
#返回两行两列的0-1随机数
#带不带size= 都一样
d=np.random.random((2,2))
print(d)
print(type(d))
#元素从2-20随机的三行三列数组
c=np.random.randint(2,20,size=(3,3))
print(c)
print(type(c))
