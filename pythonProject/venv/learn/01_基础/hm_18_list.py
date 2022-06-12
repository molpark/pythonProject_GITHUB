"""
列表的定义
List(列表)是最常用的数据类型,可以称为数组
专门用于存储一串信息
列表用[]定义,数据之间用,分隔
列表的缩影从0开始
 索引就是数据在列表中的位置编号,索引又可以被称为下标
 注意:从列表中取值时,如果超出索引范围,程序就会报错
"""

name_list=["张三","李四","王五","张三"]
print(name_list)
n=len(name_list)
print(n)
for i in range(n):
    print(i)
    print(name_list[i])

#1.知道数据的内容,想确定数据在列表中的位置
print(name_list.index("张三"))

#2.修改
name_list[1]="lisi"
print(name_list)

#3.增加
#append 方法可以向列表的末尾追加数据
name_list.append("王小二")
#insert 方法可以在列表的指定索引位置插入数据
name_list.insert(2,"小三")
#extend
#可以在列表中的末尾增加另外一个列表的完整内容
temp_list=["悟空","八戒"]
name_list.extend(temp_list)
print(name_list)

#4.删除
#remove 方法可以从列表中删除指定的数据
name_list.remove("八戒")
#pop 方法默认可以把列表中最后一个元素删除
#pop 方法可以指定要删除元素的索引
name_list.pop(2)
#clear 方法可以清空列表
#############name_list.clear()

#del关键字本质上是用来将一个变量从内容中删除
#提示:在日常开发中,要从列表删除数据,建议使用列表提供的方法
#注意:如果使用del关键字,变量将会从内存中删除
#后续的代码就不能再使用这个变量
"""
del name_list[0]
na ="xiaom"
del na
print(na)
"""

print(name_list)

#len (length 长度)函数可以统计列表中元素的总数
le_list=len(name_list)
print("列表中包含%d个元素"%(le_list))

#count 方法可以统计列表中摸一个数据出现的次数
print(name_list.count("张三"))

#从列表中删除第一次出现的数据,如果数据不存在,程序报错
name_list.remove("张三")

###列表排序
print(name_list)
num_list=[6,8,1,4,9,7]
print(num_list)

#升序
name_list.sort()
num_list.sort()
#降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
#逆反(已经排序过的list无法反转)
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)