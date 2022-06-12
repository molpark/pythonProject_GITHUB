# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class GswproPipeline:
    f=None
    #重写弗雷的一个方法:该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫........')
        self.f=open('./gsw.txt','w',encoding='utf-8')
    #专门用来处理item类型对象
    #该方法可以接收爬虫文件提交过来的item对象
    #该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        src=item['src']
        b=item['b']
        self.f.write(src+':'+b+'\n')
        return item  #写了就会传递给下一个即将被执行的管道类

    def close_spider(self,spider):
        print('结束爬虫')
        self.f.close()

#管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class mysqlPipLine(object):
    conn=None
    cursor=None
    def open_spider(self,spider):
        DBHOST = 'localhost'
        DBUSER = 'root'
        DBPASS = '12345'
        DBNAME = 'local_local'
        self.conn=pymysql.connect(host=DBHOST, user=DBUSER
                        , passwd=DBPASS, database=DBNAME,charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        sqlquery='insert into local_local.gsw values(%s,%s)'
        sqlvalue=[item['src'],item['b']]
        try:
            self.cursor.execute(sqlquery,sqlvalue)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        print('关闭连接,关闭数据库')
        self.cursor.close()
        self.conn.close()

#爬虫文件提交的item类型的对象最终会提交给哪一个管道类
    #-限制性的管道类:根据优先级,优先级越小 越早执行