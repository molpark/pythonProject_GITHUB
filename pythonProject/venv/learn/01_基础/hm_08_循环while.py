import random
var=random.randint(1,10)
print(var)
i=int(0)
while i<var:
    print("请+%.f"%i)
    i=i+1
print("结束")


for i in range(var):
    print("123")

##赋值运算符
# c+=a  c=c+a
# c-=a  c=c-a
# c*=a c=c*a
# c/=a c=c/a
# c//=a c=c//a


print("请等待")
i=0
m=0
while i<=2:
    m=m+i
    print("ishi %.f" % i)
    i=i+1
print(m)
print("结束了")

#sum的写法
num=sum(range(0,101))
print(num)


###0-100之间所有偶数只和

print("kaishi")
i=0
m=0
while i<=100:
    #偶数1%2==0
    #基数i%2!=0
    if i%2==0:
        print("i=",i)
        m+=i
        print("m=",m)
    i+=1
print("m结束")
print(m)
print(i)

print("kaishi")
i=0
m=0
while i<=100:
#偶数1%2==0
#基数i%2!=0
    if i%2==0:
        print("i=",i)
        m+=i
        print("m=",m)
        i+=1
    i += 1
print("m结束")
print(m)
print(i)


#####循环嵌套
i=1
while i<10:
    print("我不要",i)
    while i<=5:
        print("我要",i)
        i=i+1
    i=i+2

###定义一个计数器变量,从数字1开始,循环会比较方便
row =1
while row<=5:
    print("*"*row)
    row+=1

##for的写法
i=1
for i in range(10):
    print("*"*i)

###向控制台输出内容结束后,不想换行可以这么写
print ("*",end="(^_^)")
print(123)

##########嵌套循环
row =1
while row<=5:
    #每一行要打印的星星和行号一致
    #增加一个循环,负责当前行中每一列的星星
    #1.定义一个列的户数器
    col=1
    #2.开始循环
    while col<=row:
        print("*",end="")
        col+=1
    print("")
    row+=1


##99乘法表
num =1
while num<=9:
    cal=1
    while cal<=num:
        print("%d * %d =%d"%(num,cal,num*cal),end="\t")
        cal+=1
    num+=1
    print()

#字符串中的转义字符
"""
转义字符
\t 在控制台输出一个制表符,协助输出文本是垂直方向保持对齐
\n 在控制台输出一个换行符
\\ 反斜杠符号
\' 单引号
\" 双引号
\r 回车
"""

print ("1 2 3")
print("10 20 30")
print("10\t20\t30")
print("1\t2\t3")

print("hello\n python")
print("\"hello\"")
