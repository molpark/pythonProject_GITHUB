d={"name":"yishun"
   ,"age":"18"}

for i in d :
    print(i)

print("1111111111")
for i in d.keys():
    print(i)

print("222222222222")

for i in d.values():
    print(i)
print("33333333333333")

for i in d.items():
    print(i[0])

print("4444444444444444")


for i in range(5):
    for o in range(5):
        print(o,end="")
    print("")

for i in range(1,10):
    for o in range(i):
        print("{}*{}={}".format(i,o,int(i)*int(o)),end="\t")
    print("")

import time
i=9
while True:
    if i==0:
        print("结束")
        break
    else:
        print(i)
        i-=1

#要求最后数据入了信息中员工的数量和员工明细数据包含姓名和工资
# 最后算出录入员工薪资的平均值
#并且还要做退出处理,即输入X为退出
coun=0
sal=[]
name=[]
def list_dic(list1,list2):
    dic=dict(map(lambda x,y:[x,y],list1,list2))
    return dic

while True:
    inc=input("清输入操作步骤任意键进入,X退出")
    if inc=="X":
        print("退出")
        break
    else:
        name.append(input("请输入姓名\n"))
        sal.append(input("请输入薪资\n"))
        dic=list_dic(name,sal)
        print(dic)
for i in dic:

    print("姓名{},工资{}".format(i,dic[i]))

for i in dic.values():
    i=int(i)
    coun+=i

print("工资总和{}".format(coun))

