# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 0:24
# @Author  : lys
# @Project : pythonProject
# @File    : os_001_标准库.py

import os
#1.系统相关的内容
print(os.name)
#print(os.environ)  #环境变量
print(os.sep)
print(os.pathsep)
print(os.linesep) #\r\n
#2.文件和目录的操作
os.mkdir('stddemo')
os.rmdir('stddemo')
#os.makedirs()    removedirs #创建多级目录 删除多级目录
print(os.getcwd())
#rename
#路径的拆分和合并
#os.path.split()
#os.path.join()
file_path=os.getcwd()+'\测试目录'
file_path=os.path.join(os.getcwd(),'os_001_标准库.py')
print(file_path)
print(os.path.split(file_path)) #前面的元素是路径但不包含最后一个元素,后面是最后一个元素
print(os.path.isabs(file_path)) #判断是否是绝对路径


#最常用的方法
#判断是否是一个路径(文件夹),判断是否是一个文件
print(os.path.isdir(file_path))
print(os.path.isfile(file_path))

##最最常用判断文件是否存在
print(os.path.exists(file_path))

#拿到文件或者目录的最后修改时间返回的是一个时间戳
print(os.path.getatime(file_path)) #最后修改时间
print(os.path.getctime(file_path)) #最早创建时间
print(os.path.getmtime(file_path))

print(os.path.getsize(file_path)) # 查询文件大小(字节)

#删除文件
#os.remove(file_path)


#3.执行命令和管理进程
os.system('python hello.py')
