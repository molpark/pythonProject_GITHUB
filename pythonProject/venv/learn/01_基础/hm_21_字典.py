##字典的定义
"""
dictionary(字典)是除列表外python最灵活的数据类型
字典同样可以用来存储多个数据
通常用于存储描述一个物体的相关信息
和列表的区别
1.列表是有序的对象集合
2.字典是无序的对象集合
字典用{}来定义
字典使用键值对存储数据,键值对之间使用,分隔
1.键 key是索引
2.值value是数据
3.键和值之间使用:分隔
4.键必须是唯一的
5.值可以是任何数据类型,但键只能使用字符串,数字,元组
"""
#字典是一个无序的数据集合,使用print函数输出是可能顺序和定义的不一致
xiaoming ={
    "name":"xiaoming",
    "age":18,
    "gemder":True,
    "height":1.75
}
print(xiaoming)

#1.取值
#取值时如果指定的key不存在会报错
n=xiaoming["name"]
#2.增加/修改
#如果key不存在会增加键值对
#如果key存在,会修改已经存在键值对
n=xiaoming["weight"]=75
n=xiaoming["name"]="xiaohuang"
#3.删除
#在删除指定键值对是,key不存在,报错
n=xiaoming.pop("name")
print(n)
print(xiaoming)


print("----------------------")
##1.统计键值对数量
n=len(xiaoming)
##2.合并字典
temp_dict={"name":"xiaoming"}
xiaoming.update(temp_dict)
n=xiaoming
##3.清空字典
#变量n一样会被清空
#xiaoming.clear()
##测试
n=xiaoming.values()
#n=xiaoming.items()
print(n)
print(xiaoming)

##for循环
#使用多个键值对,存储描述一个物体的相关信息--描述更复杂的数据信息
#将多个字典放在一个列表中,再进行遍历
print("==========================")
card_list=[{
    "name":"zhangsan",
    "qq":"123456",
    "phone":"110"},
    {"name":"lisi",
    "qq":"654321",
     "phone":"120"
    }]


for card_info in card_list:
    print(card_info)
    print(card_info.values())