def demo(*args,**kwargs):
    print(args)
    print(kwargs)

##元组变量/字典变量
gl_nums=(1,2,3)
gl_dict={"name":"xiaoing","age":"18"}

##拆包方法和定义参数一致
#*元组,**字典
#拆包语法,简化元组变量/字典变量的传递
demo(*gl_nums,**gl_dict)