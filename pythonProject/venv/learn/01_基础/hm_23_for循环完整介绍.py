"""
for 变量 in 集合:
    循环体代码
else:
    没有通过break退出循环.循环结束后,会执行的代码

遍历完成会执行else内的代码
如果在循环体内部使用break退出,那么else的代码不会执行
"""

for i in [1,2,3]:
    print(i)
    if i>1:
        break
else:
    #如果循环体内部使用break退出了循环
    #else下方的代码就不会被执行
    print("循环结束")

##应用场景
students=[{
    "name":"xiaoming",
    "age":"18"
},
{
    "name":"xiaowang",
    "age":"17"
}]

print("-----------------")
#for下的else是等循环体所有循环都结束后再执行的
name="xiaofa"
for i in students:
    print(i)
    print(i.values())
    if i["name"]==name:
        print(name)
        break
else:
    #如果希望在搜索列表式,所有的字典检查后,没有发现目标
    print("查询结束没有找到")