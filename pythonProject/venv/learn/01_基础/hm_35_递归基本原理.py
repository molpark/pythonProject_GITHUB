#测试递归基本原理
#########################
def test01():
    print("test01")
    test02()
    test01() # 最终会报错退出,因为一直在打开新内存

def test02():
    print("test02")

#test01()

#############################
#1.终止条件
#
#2.
#先进后出的原则
##########################
def test01(n):
    print("test01",n)
    if n==0:
        print("over")
    else:
        test01(n-1)
    print("test&&&",n)

def test02():
    print("test02")
#test01(4)

###############
##递归来做阶乘
def cheng01(n):
    #print("{}*{}=".format(n,n-1),n*(n-1))
    if n==6:
        print("over")
        return 1
    else:
        ad=cheng01(n+1)
        return ad*n
if __name__ == '__main__':
    print(cheng01(1))
