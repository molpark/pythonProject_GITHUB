# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 16:23
# @Author  : lys
# @Project : pythonProject
# @File    : connect_test.py

import sqlite3
conn=sqlite3.connect('First.db')
curs=conn.cursor()
curs.execute("delete from T_fish")
#curs.execute("Create table T_fish(date text,name text,nums int,price real,Explain text)")  #根据上表结构建立对应的表结构对象
curs.execute("insert into T_fish Values('2018-3-28','黑鱼',10,28.3,'tom')")
curs.execute("select * from T_fish")
result=curs.fetchall()
print(result)
conn.commit()
conn.close()