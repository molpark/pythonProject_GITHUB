name=["zhangsan","lisi","wangwu"]
age=[18,19,20]
job=["plice","teacher","student"]


#通俗的方法是
for i in range(3):
    print("{},{},{}".format(name[i],age[i],job[i]))

#进阶的用法是,另外要注意的是zip的方法好像会改变变量
a=zip(name,age,job)
for name,age,job in a:
    print("{},{},{}".format(name,age,job))



