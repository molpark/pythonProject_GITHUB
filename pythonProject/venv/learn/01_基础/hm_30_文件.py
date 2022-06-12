"""
操作文件的函数/方法
一个函数3个方法
open (函数)打开文件,并且返回文件操作对象,默认是以只读方式打开文件
read 将文件内容读取到内存
write 将指定内容写入文件
close 关闭文件

"""

#1.打开文件
file=open("d:/test/123.txt")
#2.读写文件内容
text=file.read()
print(text)
print("-"*50)

#3.关闭文件
file.close()


file=open("d:/test/123.txt","w")
#2.读写文件内容
file.write("1")
#3.关闭文件
file.close()
"""
访问方式
f 只读方式,默认模式
w 只写方式
a 追加方式
带+的方式消耗资源,一般用以上三种方式
r+ 读写方式,文件不存在会抛出异常,文件指针在文件的开头
w+ 读写方式,文件不存在会创建文件
a+ 读写方式 文件指针在文件的结尾.文件不存在穿件文件
"""

file=open("d:/test/123.txt","a+")
#2.读写文件内容
file.write("234")
#3.关闭文件
file.close()


"""
readline方法
read方法默认会把文件所有内容一次性读取到内存中.
如果文件太对,对内存的占用会非常严重

readline方法可以一次读取一行内容
方法执行后会把文件指针移动到下一行,准备再次读取
"""

#循环读取全部内容
print("++++++++++++++")
file=open("d:/test/333.txt")
while True:
    a=file.readline()
    print(a)
    #判断是否读取到内容
    if   not a:
        break
file.close()

print (";;;;;;;;;;;")


#读取一行内容
file=open("d:/test/333.txt")
b=file.readline()
print(b)
file.close()


###文件读写的案例  --复制文件(小文件)
#1.打开源文件和目标文件
#2.读源文件写目标文件
#3.关闭文件
##没有文件会自动创建文件
print("test1")
file1 =open("d:/test/333.txt")
file2 =open("d:/test/555.txt","w")
te1=file1.read()
te2=file2.write(te1)
file1.close()
file2.close()


##读写大文件
#一次性读取大文件,会导致内存不够
print("test2"*10)
filebig1=open("d:/test/555.txt")
filebig2=open("d:/test/big.txt","w")
while True:
    text=filebig1.readline()
    if not text:
        break
    filebig2.write(text)
filebig1.close()
filebig2.close()

