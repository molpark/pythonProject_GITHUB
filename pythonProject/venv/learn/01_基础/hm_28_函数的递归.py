"""
函数的递归
函数调用自身的编程技巧称为递归
特点:
一个函数内部调用自己
 函数内部可以调用其他函数,当然也可以调用自己
代码特点:
1.函数内部的代码是相同的知识针对参数不同,处理的结果不同
2.当参数满足一个条件时,函数不再执行
  ***这个非常重要,通常被称为递归的出口,否则会出现死循环
"""
##break  的作用是退出循环可以用在while中 比如while True 是需要想办法break出来
##return的作用的跳出函数
def sum_num(num):
    print(num)
    ##自己调自己
    if num==-1:
        return
    sum_num(num-1)
sum_num(3)

##案例数字的累加
"""
定义一个函数sum_numbers
能够接受一个num的整数参数
计算1+2...num的结果
"""
print("-------------------")

def sum_numbers(num):
    #1.考虑出口
    if num == 1:
        return 1
    a=sum_numbers(num-1)
    #print(a)
    return a+num
abc=sum_numbers(10)
print(abc)

