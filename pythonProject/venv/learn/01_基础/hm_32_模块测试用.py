def ccc():
    ccc="tet"
    print(ccc)
    return ccc

a="re"

#如果直接执行模块都是__main__


#文件被导入时,能够直接执行的代码不需要被执行!
def say_hell0():
    print("nihao ")

if __name__=="__main__":
    print(__name__)
    print("小明开发的模块")
    say_hell0()
