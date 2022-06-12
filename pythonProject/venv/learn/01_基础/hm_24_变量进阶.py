n='11'
print(id(n))

print("------------------")
def test(num):
    return 500

a=10
print(id(a))

r=test(a)
print(r)


a=[123,123,123]
print(a)
print((id(a)))
a.clear()
print(a)
print(id(a))
a=[323]
print(id(a))

d={"name":"21"}
d["age"]=18
print(d)
d.clear()
print(d)


n=hash("hello12")
print(n)

num = 10

##希望修改全局变量的值,使用global声明一下变量即可
#global关键字会告诉解释器后面的变量是一个全局变量
#再使用赋值语句时,就不会创建局部变量
def chan():
    global num
    num = 100
    print(num)
chan()

print("------------------------")
###一个函数返回多个数据
##如果返回的数据类型时元组,可以省略小括号
def measure():
    print("start")
    temp="90"
    wet="50"
    print("end")
    return temp,wet
#元组
result=measure()
print(result)
for i in result:
    print(i)
##如何单独拿到变量
##如果返回的类型时元组,同时希望单独处理元组中的元素
#可以使用多个变量一次接受函数的返回结果
#这种方式更加方便
#注意:使用多个变量接受结果是,变量的个数要和元组的元素个数保持一致
gl_temp,gl_wet=measure()
print(gl_temp)
print(gl_wet)

####变量的交换
#python专有元组和列表均可
a=6
b=100
##等号右边其实是元组,只不过将括号省略掉了
a,b=b,a
print(a,b)  ##100,6
print(a)  ##100

##函数内部代码在执行时不会影响全局变量的赋值
#不会修改到外部的实参变量
#可变的列表也是不会变的
def demo(num,num_list):
    print("在函数内部,针对参数使用赋值语句")
    gl_num ="20"
    gl_num_list=[1,3,4]
    return gl_num,gl_num_list
gl_num="10"
gl_num_list=[3,3,4]
result =demo(gl_num,gl_num_list)
print(result)
print(gl_num)
print(gl_num_list)



####使用方法修改列表的内容
#全局变量会发生变化
#列表变量使用+=不会做相加的操作
#而是extend 追加的意思,所以会改变全局变量
"""但是使用a=a+a 这种就不是extend不会影响
这边是赋值的意思
"""
def demo2(num_list2):
    num_list2.append(4)

n=[1,2,3]
print(n)
demo2(n)
print(n)

n=n+n
print(n)