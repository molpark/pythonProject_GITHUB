ran=8
for i in range(ran):
    print(i)


#使用迭代遍历列表
"""
顺序的从列表中依次获取数据,每一次循环过程中,数据都会保存
在my_name这个变量中,在循环体内部可以访问到当前这一次获取到的值

for myname in 列表变量:
    print("我的名字叫%s"%myname)
"""
name_list=["zhangsan","lisi","wangwu"]
for myname in name_list:
    print("我的名字叫%s"%myname)

#list可以存储不同类型的数据
lista=["zjamh",1]
for a in lista:
    print(a)