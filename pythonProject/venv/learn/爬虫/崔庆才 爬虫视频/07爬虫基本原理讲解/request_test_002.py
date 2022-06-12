import requests


response=requests.get('https://m.weibo.com/')
print(response.status_code)
print(response.text)