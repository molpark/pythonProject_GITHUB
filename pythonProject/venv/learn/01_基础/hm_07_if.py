##比较运算符
"""
==  #判断两个操作的数的值是否相等
!=  "! =" 好像是会自动转换
>,<,>=,<=
"""

"""
if 的基本语法
顶格写if

if要判断的条件:
    条件成立时要做的事情
if语句以及缩进部分是一个完整的代码块
"""
##演练
age=18

if age>=18:
    print("年龄:%.f"%age,",可以进网吧happy")
#判断语句后续的代码和IF没有关系
print("无论何时都会执行")
##代码块看缩进,上方print没有缩进说明是独立的代码块



##else
"""
else配合if来执行的,else需要顶格写,需要添加:
if 要判断的条件:
    成立时执行
else:
     不成立时执行
     ...
"""
age=17
if age>=18:
    print("成立")
else:
    print("不成立")

##  ctrl+/ 是批量注释
##案例
#age=input("今年多大了")  ##input获得到的是字符串
age=18
print(type(age))
age=int(age)
if age>=18:    ##不同类型不能直接比较 ##此处有缩进箭头
    print("可以去网吧")
    print("可以去网吧")
    print("可以去网吧")
    print("可以去网吧")
    print("可以去网吧")
    print("可以去网吧")
else:
    print("不可以去网吧")
print("不管是否成立都会执行")
##代码块
#if和else语句以及各自的缩进部分共同是一个代码块

###逻辑运算
"""
与 and
或 or
非 not
"""

###else: if:  原始用法
a=2
b=3
if a==2 and b==4:
    print("成立")
else:
    if a==3 or b==3:
        print("11成立")
    else:
        print("11不成立")
    print("不成立")


##练习案例
age = 120
if age>=60 and age<=120:
    print("还活着")
else:
    print("死了")

## in range() 函数包前不包后
age=60
if age in range(60,120):
    print("还行")

###is_employee
#希望不成立的时候才做的事情,可以使用not运算符
#另外需要拼接复杂的逻辑运算条件时,也可能使用not
is_employee=True
if not is_employee:
    print("not employee")
else:
    print("employee")

##elfif进阶用法
age =0
if age>=10:
    print(">-10")
elif age<10 and age>0:
    print("<10")
else:
    print("不合法")

#演练
##if的嵌套,增加额外的条件
age=20
holiday="圣诞节"
if holiday=='平安节':
    print("看电影")
elif holiday=="圣诞节":
    if age>=18:
        print("去开房")
    else:
        print("看书")
else:
    print("回家")



########石头1剪刀2布3
##导入随机包,在导入工具包时应将导入语句放在文件顶部
import random

player=int(input("请出拳"))
print("玩家出拳:%d"%player)
##随机数
computer=random.randint(1,3)
print("玩家出拳是%d - 电脑出拳是%d"%(player,computer))
if player==computer:
    print("平手")
elif ((player==3 and computer==1)\
        or(player==2 and computer==3)\
        or(player==1 and computer==2)):
    print("玩家胜")
else:
    print("电脑胜")