#测试nonlocal,global关键字的用法

a=100
def test01():
    global a  ## 全局变量,当只有一层的时候global和nonlocal没区别,但此处并不能用nonlocal
    c=a+1
    return(c)

print(test01())

c=200
b=10
def test02():
    b=50
    c=300
    def inner_test02():
        global b #这时候读的最外层的全局变量b
        #如果此处不写global 那么b读到的是50 默认的是nonlocal
        #此时定义了global 如果此处重新定义b的值,那么最外层b的值也会跟着改变.
        #这边global应该还是比较常用的一个点,可以在内层改外层的全局变量的值
        print(b)
        nonlocal c #不管写不写nonlocal优先读到都是离自己最近c
        print(c)
    inner_test02()

test02() ##结果出来是10