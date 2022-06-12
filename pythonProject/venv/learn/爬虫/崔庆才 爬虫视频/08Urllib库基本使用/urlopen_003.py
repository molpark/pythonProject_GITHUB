#### 响应
import socket
import urllib.request
import urllib.error

try:
    response=urllib.request.urlopen('http://www.baidu.com',timeout=0.1)
#判断一下错误的原因
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('timeout')
'''
isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
'''
# except Exception as e:
#     print(e)

#响应类型
print(type(response))
#<class 'http.client.HTTPResponse'>

response=urllib.request.urlopen('http://www.python.org')
print(response.status)
print(response.getheaders())
#获取特定的响应头
print(response.getheader('Server'))
#获得响应体的内容 字节流的形式需要转成utf8
print(response.read().decode('utf-8'))