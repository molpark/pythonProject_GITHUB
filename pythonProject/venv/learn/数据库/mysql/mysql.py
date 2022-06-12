import pymysql
DBHOST='localhost'
DBUSER='root'
DBPASS='123'
DBNAME='db_lu'

try:
    db=pymysql.connect(host=DBHOST,user=DBUSER
                       ,passwd=DBPASS,database=DBNAME,charset='utf8')
    print('数据库连接成功')
    #开游标
    cur=db.cursor()
    #创建及删除表语句
    cur.execute('drop table if exists lu20211031test')
    sql='create table lu20211031test(name varchar(20),age int)'
    cur.execute(sql)
    #插入数据记得需要commit
    sqlquery1="insert into lu20211031test values(%s,%s)"
    sqlvalue1=['xiaoli',40]
    sqlvalue2 = ['xiaowang', 39]
    cur.execute(sqlquery1,sqlvalue1)
    cur.execute(sqlquery1, sqlvalue2)
    db.commit()
    #查询数据,使用fetchall()方法接收全部的返回结果
    sqlquery2='select * from lu20211031test'
    cur.execute(sqlquery2)
    result=cur.fetchall()
    for i in result:
        print(i)
    #更新表中的数据
    sqlquery3="update lu20211031test set name =%s where name=%s"
    upvalue=['xiaoyue','xiaowang']
    cur.execute(sqlquery3,upvalue)
    db.commit()
    #删除表中的数据
    sqlquery4="delete from lu20211031test where name =%s"
    devalue='xiaoyue'
    cur.execute(sqlquery4,devalue)
    db.commit()
    #删除一张表
    sqlquery5="drop table if exists lu20211031test"
    cur.execute(sqlquery5)
except Exception as e:
    print("失败原因:"+str(e))
    db.rollback()
db.close()
