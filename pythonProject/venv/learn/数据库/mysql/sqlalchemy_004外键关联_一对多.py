#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from  sqlalchemy.orm import sessionmaker,relationship
# 创建数据库
engine = create_engine("mysql+pymysql://root:123@localhost:3306/db_lu", max_overflow=5)
# 生成一个SqlORM 基类
Base = declarative_base()
# 定义表结构
class User(Base):
    # 表名
    __tablename__ = 'user'
    # 定义id,主键唯一,
    id = Column(String, primary_key=True)
    name = Column(String(50))
    books=relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    # id字段
    id = Column(String(20), primary_key=True)
    # 名字字段
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    # ForeignKey是外键 关联user表的id字段并且需要类型一致
    user_id = Column(String(20), ForeignKey('user.id'))


# 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
Base.metadata.create_all(engine)


if __name__ == '__main__':

    # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    Session = sessionmaker(bind=engine)
    session = Session()
    # 获取session，然后把对象添加到session

    liuyao=User(id='1',name='liuyao')
    ali=User(id='2',name='ali')
    session.add_all([liuyao,ali])
    session.commit


    ##增加book字段
    # 创建白鹿原这本书，指定谁是拥有者
    Whitedeer = Book(id='1', name='White_deer', user_id='1')
    # 创建三体这本书，指定谁是拥有者
    Threebody = Book(id='2', name='Three_body', user_id='2')
    # 添加字段
    session.add_all([Whitedeer, Threebody])
    # 提交
    session.commit()















# 最后提交并关闭。Session对象可视为当前数据库连接。
session.close()