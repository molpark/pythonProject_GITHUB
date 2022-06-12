import requests
import re


def start(cookie):
    for w in range(0, 1600, 32):
    #页码根据实际情况x32即可，我这里是设置50页为上限，为了避免设置页码过高或者数据过少情况，定义最大上限为1600-也就是50页，使用try-except来检测时候异常，异常跳过该页，一般作为无数据跳过该页处理
        # 注意uuid后面参数空余将uuid后xxx替换为自己的uuid参数
        try:
            url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=67e5f69f0a6446898268.1619358457.1.0.0&userid=-1&limit=32&offset='+str(w)+'&cateId=-1&q=%E7%81%AB%E9%94%85'
            #headers的数据可以在F12开发者工具下面的requests_headers中查看，需要实现选择如下headers信息
            #必要情况  请求频繁 建议增加cookie参数在headers内
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
                'Host': 'meituan.com',
                'Origin': 'https://sh.meituan.com',
                'Referer': 'https://sh.meituan.com/s/%E5%BC%A0%E4%BA%AE%E9%BA%BB%E8%BE%A3%E7%83%AB/',
                'Cookie': cookie
            }
            response = requests.get(url, headers=headers,allow_redirects=False)
            print(response)
            #正则获取当前响应内容中的数据，因json方法无法针对店铺特有的title键值进行获取没所以采用正则
            titles = re.findall('","title":"(.*?)","address":"', response.text)
            addresses = re.findall(',"address":"(.*?)",', response.text)
            avgprices = re.findall(',"avgprice":(.*?),', response.text)
            avgscores = re.findall(',"avgscore":(.*?),',response.text)
            comments = re.findall(',"comments":(.*?),',response.text)
             #输出当前返回数据的长度  是否为32
            print(len(titles), len(addresses), len(avgprices), len(avgscores), len(comments))
            for o in range(len(titles)):
             #循环遍历每一个值  写入文件中
                title = titles[o]
                address = addresses[o]
                avgprice = avgprices[o]
                avgscore = avgscores[o]
                comment = comments[o]
                 #写入本地文件
                file_data(title, address, avgprice, avgscore, comment)
        except Exception as e:
            print(e)

#文件写入方法
def file_data(title, address, avgprice, avgscore, comment):
    data = {
                '店铺名称': title,
                '店铺地址': address,''
                '平均消费价格': avgprice,
                '店铺评分': avgscore,
                '评价人数': comment
            }
    with open('d:/test/food.txt', 'a', encoding='utf-8')as fb:
        fb.write(json.dumps(data, ensure_ascii=False) + '\n')
        #ensure_ascii=False必须加因为json.dumps方法不关闭转码会导致出现乱码情况
if __name__ == '__main__':
    cookie='uuid=67e5f69f0a6446898268.1619358457.1.0.0; _lx_utm=utm_source=Baidu&utm_medium=organic; _lxsdk_cuid=179094bb057c8-04dd9f3b789f45-353c540f-100200-179094bb057c8; mtcdn=K; lt=hRO5Ep2Y4iBovQBR7h-lraVYz-wAAAAAZg0AAON6rXAxhm964rAcdcrM4XfdYM5J3ze2COS-WCKUVH3imxTMYzSJ6CGphCNpPY_gGg; u=731230722; n=卢一顺; token2=hRO5Ep2Y4iBovQBR7h-lraVYz-wAAAAAZg0AAON6rXAxhm964rAcdcrM4XfdYM5J3ze2COS-WCKUVH3imxTMYzSJ6CGphCNpPY_gGg; unc=卢一顺; _hc.v=ae6750b1-f836-f7a1-a3bc-6681ed9c1229.1619358675; lat=31.391232; lng=121.23799; _lxsdk=179094bb057c8-04dd9f3b789f45-353c540f-100200-179094bb057c8; ci=10; rvct=10,1; firstTime=1619360474129; __mta=244210234.1619358635796.1619359887080.1619360475145.3; _lxsdk_s=179094bb058-f78-449-93b||65'
    cookie=cookie.encode("utf-8").decode("latin1")
    start(cookie)