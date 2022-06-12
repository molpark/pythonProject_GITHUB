import requests
response=requests.get('http://www.baidu.com')
#获取网页源代码
print('text:  '+response.text)
#获取响应头
print('header: '+str(response.headers))
#状态码
print(response.status_code)

#使用headers 发起请求
headers={}
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
response=requests.get('http://www.baidu.com',headers=headers)
print(response.status_code)


print('****************************************')
#获取图片
#https://www.baidu.com/img/flexible/logo/pc/result.png
response=requests.get('https://static.zhihu.com/heifetz/favicon.ico',headers=headers)
print(response.content)

with open(r'C:\job\learning\pythonProject\venv\learn\爬虫\崔庆才 爬虫视频\test\result.ico','wb') as f:
    f.write(response.content)
    f.close()