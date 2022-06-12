
#打开chrome 浏览器访问指定页面

from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://m.weibo.com')
driver.get('http://www.zhihu.com')