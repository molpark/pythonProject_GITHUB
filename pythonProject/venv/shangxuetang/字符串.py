try:
    a=1
    b="2"
    c=a+b
    print(c)
except Exception as e:
    print(e)

a=520
print(type(a))
c=str(a)
print(type(c))


a="1234567890"
print(a[-1])


##需要注意的是replace完产生的是一个新的字符串,要用新的变量去接收,原有的变量并不会改变
a.replace('0','-')
print(a)
b=a.replace('0','-')
print(b)

#字符串的截取
b=a[1:8:2]  ##步长为2意思隔一个取一个
print(b)

##split分割和join 合并
#split 要赋值到新的变量中才能识别到,原有的变量不做变化
a="0,1,2,3,4"
b=a.split(',')
print(b)
#join 比+更好节省对象的生成
c=','.join(b)
print(c)

##包的导入
#包的复用
from  hm_message import receive_message as e
a=e.receive()
print(a)


a="1"
b="1,2,3,44"
if a in b:
    print("zai")
elif a not in b:
    print("buzai")


a="""{a}想要买{b}""".format(a="我",b="鞋")
print(a)

#format 的填充方法
a="""{a}喜欢的数字是{b:*^8}""".format(a="wo",b=6)
print(a)

a=123.33333
b="{:.2f}".format(a)
print(b)


for i in "abc":
    print(i,end="w\t")