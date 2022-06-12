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

####  添加 ########
# 定义一个字段
zengjia = User(id=2, name='sbliuyao')
# 添加字段
session.add(zengjia)
# 添加多个字段
session.add_all([
    User(id=3, name='sbyao'),
    User(id=4, name='liuyao')
])






# 提交以上操作，现在只是在内存中增加，回写到数据库，就必须做提交操作
session.commit()
session.close()

