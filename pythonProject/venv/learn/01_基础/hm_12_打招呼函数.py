
##只代表函数封装好,不主动调用,是不会执行的
def say_hello():
    """打招呼注释"""
    print("hello 1")
    print("hello 1")
    print("hello 1")

name ="xiaoming"
print (name)
say_hello()
print(name)

"""
补充一个调试方式
F8 STEP OVER 可以单步执行代码,但是会将函数调用中的代码一并执行
F7 SETP INTO 可以单步执行代码,函数是会进入内部一步步执行
"""