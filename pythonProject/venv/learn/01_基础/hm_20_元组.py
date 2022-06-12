"""
元组的定义
tuple与列表类似,不同之处在于元组的元素不能修改
元组表示多个元素组成的序列
有特定的应用场景
1.用于存储一串信息,"数据之间用,分隔"
2.元组用()定义
3.元组的索引从0开始
"""
info_tuple=("zhangsan",18,1.75)
print(info_tuple)
print(type(info_tuple))
print(info_tuple[0])
print(info_tuple[1])
print(info_tuple[2])

#创建空元组
empty_tuple=()

#创建只有一个元素的元组
single_tuple=(5)
print(type(single_tuple))   ##int类型
single_tuple=(5,)
print(type(single_tuple))  ##<class 'tuple'>

##元组的常用操作
single_tuple=("zhangsan",18,1.75)
#统计包含的元素个数
n= len(single_tuple)
#数据出现的次数
n=single_tuple.count(18)
#取索引,已经知道数据的内容,要知道数据在元组中的索引
n=single_tuple.index("zhangsan")
print(n)

##元组变量的循环遍历
"""
for循环遍历所有非数字型类型的变量:列表,元组,字典以及字符串
提示:在实际开发中,除非能确认元组中的数据类型,否则针对元组的循环
遍历需求并不是很多
"""

for i in single_tuple:
    print(i)


##格式haul字符串后面的'()'本质上就是元组
print("%s年龄是%d身高是%.2f"%single_tuple)
info_str="%s年龄是%d身高是%.2f"%single_tuple
print(info_str)

##元组和列表之间的转换
print(type(single_tuple))
single_tuple=list(single_tuple)
print(type(single_tuple))
single_tuple=tuple(single_tuple)
print(type(single_tuple))