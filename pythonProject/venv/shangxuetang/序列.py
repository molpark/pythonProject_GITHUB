##列表

a=[0,1,2,3,4,5,6]
a.append(7)
print(a)
a.extend("8")
print(a)

a= list(range(1,10))
print(a)

a.insert(-1,"10")
print(a)

x=[x*2 for x in range(10) if x%4==0]
print(x)


a=[1,2,3,4,5]
b=a.index(4)
print(b)

import random
random.shuffle(a)
print(a)



a= [[1,2],5,6]
for i in a :
    print(a)


print("------------------")

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
d=a+b+c
print(d)
e=zip(a,b,c)
print(e)
e=list(e)
print(e)


print("222222222222")
s=(x*2 for x in range(10))
print(s)
s1=s.__next__()
print(s1)
s2=s.__next__()
print(s2)