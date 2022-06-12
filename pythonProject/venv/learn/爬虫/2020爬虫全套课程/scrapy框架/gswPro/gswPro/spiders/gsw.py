import scrapy
from gswPro.items import GswproItem

class GswSpider(scrapy.Spider):
    name = 'gsw'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']

    #基于命令存储数据的解析方法
    # def parse(self, response):
    #     #解析名称+内容
    #     div_list=response.xpath('//*[@id="main"]/div[3]/ul/li//img')
    #     #print(div_list)
    #     all_data=[] #存储所有解析到的数据
    #     for div in div_list:
    #         #xpath返回的是列表,但是列表原色一定是selector类型的对象
    #         #extractor可以将selector对象中data参数存储的字符串提取出来
    #         #列表调用了extract之后,则表示将列表中每一个selector对象中data对应的字符串提取了出来
    #         src=div.xpath('./@src').extract()
    #         src = div.xpath('./@src')[0].extract()
    #         b=div.xpath('./@alt')[0].extract()
    #         #如果列表中只有一个元素可以通过extract_first() 提取出第一个字符串
    #         b=div.xpath('./@alt').extract_first()
    #         #如果b是列表
    #         #b=''.join(b)
    #         dic={
    #             'src':src,
    #             'b':b
    #         }
    #         all_data.append(dic)
    #     return all_data

    def parse(self, response):
        # 解析名称+内容
        div_list = response.xpath('//*[@id="main"]/div[3]/ul/li//img')
        # print(div_list)
        all_data = []  # 存储所有解析到的数据
        for div in div_list:
            # xpath返回的是列表,但是列表原色一定是selector类型的对象
            # extractor可以将selector对象中data参数存储的字符串提取出来
            # 列表调用了extract之后,则表示将列表中每一个selector对象中data对应的字符串提取了出来
            src = div.xpath('./@src').extract()
            src = div.xpath('./@src')[0].extract()
            b = div.xpath('./@alt')[0].extract()
            # 如果列表中只有一个元素可以通过extract_first() 提取出第一个字符串
            b = div.xpath('./@alt').extract_first()
            #将解析的数据封装存储到item类型的对象中
            item=GswproItem()
            item['src']=src
            item['b']=b
            yield item #将item提交给了管道
