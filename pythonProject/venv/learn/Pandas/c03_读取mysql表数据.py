import pandas as pd
import pymysql

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='12345',
    database='local_local',
    charset='utf8'
)
mysql_page=pd.read_sql('select * from test',con=conn)
#print(mysql_page)
#结果集.values循环获取为单行列表
for row in mysql_page.values:
    print(row)

'''
##从presto 读取数据
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
import pandas as pd
# Presto
engine = create_engine('presto://192.168.104.120:9111/hive/myhive')  # host是服务器ip，port是端口，hive指的是Presto的catalog，my_schema是hive的schema。
df = pd.read_sql("select * from employee",engine) # 和一般pandas从数据库中读取数据无任何区别，分析师们应该非常熟悉了。
print(df)
'''
