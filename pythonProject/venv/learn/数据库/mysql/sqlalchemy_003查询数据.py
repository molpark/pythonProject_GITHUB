#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# 创建数据库
engine = create_engine("mysql+pymysql://root:123@localhost:3306/db_lu", max_overflow=5)
# 生成一个SqlORM 基类
Base = declarative_base()
# 定义表结构
class User(Base):
    # 表名
    __tablename__ = 'users'
    # 定义id,主键唯一,
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
# 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
Base.metadata.create_all(engine)
# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = sessionmaker(bind=engine)
session = Session()
# 获取session，然后把对象添加到session
# 最后提交并关闭。Session对象可视为当前数据库连接。


#filter 相比于filter_by更好用 filter_by 只能用于= 的情况
#filter 能有== > < != 的用法

#查询方法0
#查询表中所有数据
ret=session.query(User).all()
print(ret)
for i in ret:
    print(i.name)
print('####################################')
#查询方法1
#查询User表中name='liuyao'的所有的值
ret=session.query(User).filter(User.name=='liuyao').all()
print(ret)#输出的是对象的内存地址
#格式是列表
for i in ret:
    print(i.name)#输出的是name字段值

print('####################################')
#查询方法2
#查询User表中name='liuyao'的第一条值
ret=session.query(User).filter(User.name=='liuyaosb').first()
print(ret)
print(ret.id,ret.name)
print('####################################')

### 查询方式3 ###
# 查询user表里字段是name是liuyao或者mayun的信息打印出来
ret=session.query(User).filter(User.name.in_(['liuyao','sbyao'])).all()
for i in ret:
    print(i.name)
print('####################################')

### 查询方式4 ###
# 可以给返回的结果起一个别名，或者叫标签：可有可无
#感觉这个方法用处不大
ret = session.query(User.name.label('')).all()
# 这里的关键是label方法，它的意思是把User的name字段改个名字叫name_label,
# 其相当于执行了：select users.name as name_label from User
print(ret,type(ret))
for i in ret:
    print(i)
print('####################################')

### 查询方式5 ###
# 查询User表根据id排序
ret=session.query(User).order_by(User.id).all()
for i in ret:
    print(i.id,i.name)
print('####################################')

### 查询方式6 ###
# 查询user表里根据id排序输入0到3的字段
#[0;3]一样适合其他查询语句,类似limit 3
ret = session.query(User).order_by(User.id)[0:3]
print(ret)
for i in ret:
    print(i.name)
print('####################################')

### 查询方式7 ###
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
ret=session.query(User).filter(User.name=='liuyao').one()
print(ret)
print(ret.name)


###关闭session
session.close()