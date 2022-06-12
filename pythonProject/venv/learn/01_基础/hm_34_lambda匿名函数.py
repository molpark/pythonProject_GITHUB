#测试lambda表达式,匿名函数
f=lambda a,b,c:a*b*c
print(f(1,2,3))
h=f(8,7,7)
print(h)

def lamtest(a,b,c):
    return(a*b*c)

if __name__ == '__main__':
    e=lamtest(2,3,4)
    print(e)

##进阶用法,返回的就是一个列表
g=[lambda c:c*2,lambda b:b*3]
print(g[0](6),g[1](3))