##函数十分抢单--将字符串当成有效的表达式来求值并返回计算结果
text=input("请输入算术题")
a=eval(text)
print(a)

def ccc():
    ccc="tet"
    print(ccc)

##eval可以执行字符串
#需要注意的是""中只能使用'',无法在所有层都用一种引号
#eval中也可以传入变量,可以是动态的
eval("print('nihao')")
