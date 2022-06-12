a=[1,2,2,2,3,4,4,5]
b={}
for i in a:
    if a.count(i)>1:
        b[i]=a.count(i)
print(b)
print(b.keys())
for i in b.keys():
    print(i)

print("---------")

from collections import Counter
a=[1,2,2,2,3,4,4,5]
c=Counter(a)
print(c)
dd=c.items()
for i in dd:
    if i[1] != 1:
        print(i[0])


print("------------")

a=[1,2,2,2,3,4,4,5]
myset = set(a)
print(myset)
for i in myset:
    b=a.count(i)
    if b>1:
        print(i)
gh=[(1,2),(2,3)]
cccc=dict(gh)
print(cccc)