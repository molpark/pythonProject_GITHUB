def num(num,*nums,**person):
    print(num)
    print(nums)
    print(person)

num(12,12,23,45,name="lisi",age="18")
"""
传入参数的方式较以往不太一样
这里12作为数字
12,23,45作为元组
name="lisi",age="18" 作为字典
"""

##案例演练
print("--------------------------")
def sum_numbers(*args):
    num=0
    print(args)
    for i in args:
        i+=i
    return i

result=sum_numbers(1,2,3)
print(result)

#如果不用多值参数,那么需要在调用函数时多加一个()
#result=sum_numbers((1,2,3))