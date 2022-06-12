"""
文件/目录的常用管理操作
py中,如果希望童工程序实现功能,需要不导入os 模块
文件操作
1  rename  重命名文件
2  remove  删除文件

目录操作
listdir 目录列表
mkdir   创建目录
rmdir   删除目录
getcwd  获取当前目录
chdir   修改工作目录
path.isdir  判断是否是文件

"""
import os
os.remove("d:/testlys/111.txt")
os.rmdir("d:/testlys")
d=os.mkdir("d:/testlys")
print(d)  ##为什么返回值是None
c=os.chdir("d:/testlys")
print(c)
file=open("d:/testlys/111.txt","w")
text=file.write("asdsa")
file.close()
a=os.listdir()
print(a)


