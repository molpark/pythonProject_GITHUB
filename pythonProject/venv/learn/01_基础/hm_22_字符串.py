
#字符串
#大多数编程语言都是用""来定义字符串
c="hello world"
c='hello world'
for i in c:
    print(i)

#使用''的情况,可以把""单独打印出来
str='"luyishun"'
print(str)


n=str.index("l")
n=str[1]
n=len(str)##str的长度或者数量
n=str.count("l")##l出现次数
#如果使用index方法字符串不存在会报错
n=str.index("l")##l的位置
print(n)


##1.判断空白字符
##\t\n\r都属于空白符
str=" \t\n\r"
n=str.isspace()
print(n)

#2.判断字符串中是否只包含数字
#unicode字符串 \u00b2
#从上到下可以判断的范围越来越大
#程序开发时一般都是使用isdecimal来判断
num_str="\u00b2"
n=num_str.isdecimal()#只能判断是否全角数字(整数)
m=num_str.isdigit()#判断全角数字(整数),(1),\u00b2
i=num_str.isnumeric()#判断全角数字(整数),(1),汉字数字
print(n)
print(m)
print(i)

print("------------------")
##3.字符串的查找和替换
str="hello world"
a=str.startswith("h")
print(a)
b=str.endswith("d")
print(b)
#index方法,如果指定的字符串不存在会报错
#find方法,如果指定的字符串不存在结果是-1
c=str.find("e")
print(c)
#replace方法执行完成后,会返回一个新的字符串,不会修改原有字符串的内容
n=str.replace("he","ab")
print(n)

##4.文本对齐
#居中
str="wqeqwe"
print(str)
a=str.center(10)
b=str.center(10," ")
print(a)
print(b)

#左对齐
c=str.ljust(10," ")
print(c)

#右对齐
d=str.rjust(10," ")
print(d)

##去掉空白字符
#比如含有\t\n等特殊字符可以通过strip
str="    abc   "
e=str.strip()
print(e)
e=str.lstrip()
print(e)
e=str.rstrip()
print(e)

print("---------------")
###split方法,join方法
##1.拆分字符串
str ="a\tb\tc\td"
print(str)
#不传参会以所有空白符作为分隔符
n_list=str.split("\t")
print(n_list)
print(type(n_list))##list类型

##2.合并字符串
m_list=" ".join(n_list)
print(m_list)
print(type(m_list))##str类型

print("=======================")
##字符串的切片
num="0123456789"
#1.截取2~5位置的字符串
a=num[2:6]
#2.截取从2~末尾的字符串
a=num[2:]
#3.几区从开始~5位置的字符串
a=num[0:6]   #num[:6]  从头开始可以省略0
#4.截取完整的字符串
a=num[0:]  #[:]
#5.从开始位置每个一个字符串截取字符串
a=num[::2]
#6.从索引1开始每隔一个取一个
a=num[1::2]
#7.截取从2~末尾-1的字符串
a=num[2:-1]
#8.截取字符串末尾的两个字符
a=num[-2:]
#9.字符串的逆序 步序指定-1就行了从右向左切
a=num[0:0:-1]
print(a)



##高级数据类型的公共方法
"""
内置函数
len() 计算容器中元素的个数
del() 删除变量
max() 返回容器中元素最大值
min() 返回容器中元素最小值
"""
a=[1,2,3]
del a[1]   ##删变量中的元素
print(a)
del(a)   ##删变量
#print(a)


str="2321412523fsdfsddg"
n=max(str)
print(n)
m=min(str)
print(m)
t_list=[3,4,6,9]
m=min(t_list)
print(m)
t_dic={"a":"2" , "b":"1"}
#字典的大小只比较key
t=max(t_dic)
print(t)


####切片
#切片使用索引值来限定范围,从一个大的字符串中切出小的字符串
#列表和元组都是有序的集合,都能够通过索引值获取到相应的数据
#字典是一个无序的集合,是使用键值对来保存数据的
#字典没有索引

##list
a=[0,1,2,3,4][1:3]
print(a)
##元组
b=(0,1,2,3,4)[1:3]
print(b)
#字典不能切片

##数据类型的运算符
"""
+ 合并  (字符串列表元组) 例 [1,2]+[3,4] =[1,2,3,4]
* 重复
in (字符串,列表,元组,字典) 例 3 in [1,2,3] 返回True
"""
a=[1,2]*5
a=(1,2)*5
print(a)
#字典不能用此方法,因为key是唯一的

b=[1,2]+[3,4]  #会产生一个新的列表
c="12"+"34"
print(b)
print(c)
b.extend([5,6])#在原有的列表基础上增加,无法赋值到新的变量
print(b)
b.append(7)#在原有的列表基础上增加,无法赋值到新的变量
b.append([8,9]) #此方法可以在列表中增加列表
print(b)

##in ,not in 在对字典操作时,判断的是字典的key(成员运算符)

a="a"
b="abcds"
n=a in b
m = a not in b
print(n)
print(m)
#字典比对的是key,不看值
print("a" in {"a":"laowang"})