from bs4 import BeautifulSoup  ##网页解析获取数据
import re   ##正则表达式,进行文字匹配
import urllib.request,urllib.error #指定url获取网页数据
import xlrd #进行excel操作
import sqlite3  ##进行sqlite数据库操作

##爬取网页
def getData(baseurl):
    datalist=[]
    #2.逐一解析数据
    return datalist

#3.保存数据
def saveData(savepath):
    pass


def main():
    print("hello")
    """
    1.爬取网页
    2.逐一解析数据
    3.保存数据
    """
    baseurl="https://movie.douban.com/top250?start=0"
    ##1.爬取网页
    datalist=getData(baseurl)
    #3.保存数据
    savepath=".\\doubandianying.xls"
    saveData(savepath)

if __name__=="__main__":  #当程序执行时调用函数
    main()