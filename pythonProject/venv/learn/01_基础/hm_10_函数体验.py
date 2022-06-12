##函数的封装
#案例99乘法表
def multiple_table():
    num =1
    while num<=9:
        cal=1
        while cal<=num:
            print("%d * %d =%d"%(num,cal,num*cal),end="\t")
            cal+=1
        num+=1
        print()

def abc():
    print(123)