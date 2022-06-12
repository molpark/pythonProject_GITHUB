import urllib.request
import urllib.parse


'''
urlopen 不带data 是get 请求
带了data 是post请求
'''

data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())