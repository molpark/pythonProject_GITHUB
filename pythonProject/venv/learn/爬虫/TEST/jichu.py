print("nihao")

if True:
    print("True")
else:
    print("False")

for i in range(5):
    print(i)

for i in range(1,3):
    print(i)

for i in range(1,10,3):
    print(i)


try:
    print(num)
    f=open("text.txt")
    print(f)
except (FileNotFoundError,NameError) as e:  ##异常类型想要被捕获到,需要一直
    print(e)

##捕获所有的异常

try:
    print(num)
    f=open("text.txt")
    print(f)
except Exception as e:  ##可以承接所有异常
    print(e)


##try except finally的嵌套
import time
try:
    f = open("text.txt")
    try:
        f=open("text.txt")
        print(f)
        while True:
            txt=f.read()
            if len(txt)==0:
                break   ##强制break掉会导致文件无法关闭所以增加一步finally 让关闭文件的操作强制执行
        time.sleep(2)
    finally:
        f.close()
        print("zhixngwanbi")
except Exception as e:  ##可以承接所有异常
    print(e)

##不在外层finally的原因是finally外的try中open是读不到了.所以close不了.所以只能在open的内层做close

def hell():
    print("hello")