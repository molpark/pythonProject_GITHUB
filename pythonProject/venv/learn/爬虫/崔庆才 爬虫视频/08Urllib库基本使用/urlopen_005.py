##更复杂的请求

from urllib import request,parse
url='http://httpbin.org/post'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
         'Host':'httpbin.org'}
dict={'word':'hello'}
data=bytes(parse.urlencode(dict),encoding='utf8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
#有单独添加header的方法
#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36')
response=request.urlopen(req)
print(response.read().decode('utf-8'))