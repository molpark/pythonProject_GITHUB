# import keyword
# print(keyword.kwlist)
#
# a=1
# b=2
# print(b)


# import numpy as np
# print(np.pi)
#
# b=3.14
# c=int(b)
# print(c)
# print(3//2)
# print("a"=="a")


#a=[1,2,3,4,5]
# b=[]
# c=list("sadsafasfsafas")
# print(c)
# print(a[-1])
# a.append(6)
# print(a)
# print(a[:3])
# print(a[::-1])
# a[1]='woshi'
# print(a)
# a.extend([7,8,9])
# print(a)
# a.append([10,11,12])
# print(a)
# a.pop()
# print(a)
# a.pop(0)
# print(a)
# # del a
# cou=a.count(1)
# print(cou)
# print(a.index(4))
# a.insert(0,'itt')
# print(a)
# a.remove(a[0])# 移除某个值第一次出现的地方
# print(a)
# a.reverse()
# print(a)
# a.pop()
# a.sort()
# print(a)
# print(len(a))


# a=(1,2,3,4)
# print(type(a))


# a= {1,2,3,4,5,5,'set'}
# print(type(a))
# #无序且不重复
# a=set([1,2,3,4,5,6])
# print(type(a))
# a.add(10)
# print(a)
# a.remove(10)
# print(a)
#
# print({1}.issubset(a))


# dict1={'name':'peter'
#        ,'age':'18'}
# print(dict1)
# a=dict(name='xiaoming')
# print(a)
#
# a['city']='chengdu'
# print(a)
#
# if 'city' in a:
#     print("ok")
#
# print(a.get('city',1))
# print(a.keys())
# print(a.items())
# for i in a.keys():
#     print(a[i])
#
#
# print("---------------------")
# for i in  a.items():
#     print(i[1])
#


# def a():
#     print("ov"+1)
#
# try:
#     if __name__=="__main__":
#         a()
# except Exception as e:
#     print(e)

# ab =['a','v','v']
# for i,j in enumerate(ab):  ##枚举
#     print(i,j)
#
# list1=[1,2,3,4]
# list2=['a','b','c','d']
# e=np.argmin([1,2,3,4])  ##找最小值对应的位置
# c=list(zip(list2,list1))
# print(c)
#
#
# import math
# d=math.floor(4.7)
# print(d)
# d=math.ceil(4.7)
# print(d)


# import numpy as np
# e=np.min([1,2,3,4])  ##找最小值
# print(e)
# print(e)


# def ex(a,b):
#     x=a**b
#     return x
#
# n=ex(3,2)
# print(n)
#
#
# def avg(x):
#     re=sum(x)/len(x)
#     return re
#
# n=avg([1,2,3,4])
# print(n)
#


def x(a,b):
    c = 0
    re=0
    for i in range(b):
        if i>a:
            c=i
        elif i<b and i>a :
            i=i+1
            re=c+i
    return re
nn=x(11,41)
print(nn)