name ="小明"
age=24.5
sex="男"
height=175
print("姓名:",name,"\n","年龄:",age)
gender=True   ##需要注意大小写
gender=False
print(gender)

##查看变量类型
print(type(name))
print(type(gender))
print(type(2**64))
###没有long类型都只有int(python3特有)
print(2**64)





##bool类型在数学计算是TRUE为1 false为0
i=10
f=10.5
b=True
res=i+f+b
print(res)

##字符串拼接
first_name="john"
second_name='lu'
res=first_name+'.'+second_name
print(res)

##字符串变量不能输数字变量相加



#input函数 输入函数
#var=input("00000000000")
#print(var)
#print(type(var))


##类型转换
var=int('21321455')
print(var)
print(var+1)
var=float(var)
print(type(var))


##字符串拼接,并且数字类型还能指定精度
price=9.000000
desc="苹果单价%.02f元"%price
print(desc)

name ="小明"
desc ="我的名字叫%s"%name
print(desc)

"""
格式化字符
%s 字符串
%d 有符号十进制整数 %06d表示输出的整数显示位数,不足会补全
%f 浮点数  %.0f表示小数点后显示两位
%% 输出%
"""

#补全
num=1
desc="学号%06d "%num
print(desc)

###案例
price =8.5
weight =7.5
money=price*weight
print("单价%.1f 重量%.1f金额%.1f "%(price,weight,money))


#定义一个小数scale 输出数据比例是10.00%
scale =0.25
print("数据比例是%.2f%%"%(scale*100))

import keyword
print(keyword.kwlist)

##变量命名要以小小命名
andy_age="333"
print(andy_age)


