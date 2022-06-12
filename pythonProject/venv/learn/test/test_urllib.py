import urllib.request as ur

#获取一个get请求
# response=ur.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  ##建议对返回来的网页源码用utf-8的方式进行解码

#获取一个post请求
#http://httpbin.org/post
#模拟用户真实登录
# import urllib.parse as up
# data=bytes(up.urlencode({"name":"lys"}),encoding="utf-8")
# response=ur.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))  ##建议对返回来的网页源码用utf-8的方式进行解码

#超时处理举例子将时间特地设置成0.01
# try:
#     response=ur.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except Exception as e:
#     print(e)

##418发现是爬虫,你需要伪装User-Agent
#import urllib.parse as up
# url="http://httpbin.org/post"
# data=bytes(up.urlencode({"name":"lys"}),encoding="utf-8")
# #可以指定headers
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
# ret=ur.Request(url,headers=headers,method="POST",data=data)
# response=ur.urlopen(ret)
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))
# print(response.read().decode("utf-8"))


url="http://www.douban.com"
#可以指定headers
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
req=ur.Request(url,headers=headers)
response=ur.urlopen(req)
print(response.read().decode("utf-8"))