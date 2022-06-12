# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 14:52
# @Author  : lys
# @Project : pythonProject
# @File    : 3线程池在爬虫案例中的应用.py

#原则:线程池处理的是阻塞且耗时的操作
#需求对梨视频的生活页面中热门视频下所有视频进行爬取
import time
import requests
from lxml import etree
from multiprocessing.dummy import Pool as threadPool

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
session=requests.session()
url_sh='https://www.pearvideo.com/category_5'

#获取生活页面中最热视频的各个链接地址
def get_sh_detail(url):
    response=session.get(url=url,headers=headers)
    page_text=response.text
    etree.HTMLParser(encoding='utf-8')
    tree =etree.HTML(page_text)
    r=tree.xpath('//*[@id="listvideoListUl"]/li/div/a/@href')
    rm_url=[]
    for i in r:
        rm_url.append(i)
    #print(rm_url)
    return(rm_url)

#针对各个链接地址中视频的src信息拿到视频的请求地址
def get_rm_detail(url):
    video_url_list=[]
    for i in url:
        contId=i.split('_')[1]
        Referer='https://www.pearvideo.com/'+i
        #print(contId)
        #print(Referer)
        video_head_url='https://www.pearvideo.com/videoStatus.jsp'
        params ={
            'contId': contId
        }
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
            'Referer': Referer
        }
        response=requests.get(url=video_head_url,headers=headers,params=params)
        page_text=response.json()
        #print(page_text)
        video_url=page_text.get('videoInfo').get('videos').get('srcUrl')
        #print(video_url)
        new_url_org = video_url.split('/')
        #print(new_url_org)
        new_url = video_url.split('/')[6]
        new_url_re=video_url.split('/')[6].split('-')[0]
        cont_n_id='cont-'+contId
        #print(cont_n_id)
        new_url_re_s=new_url.replace(new_url_re,cont_n_id)
        #print(new_url_re_s)
        #修改列表
        new_url_org.remove(new_url)
        new_url_org.append(new_url_re_s)
        new_url_org='/'.join(new_url_org)
        #print(new_url_org)
        video_url_list.append(new_url_org)
    #print(video_url_list)
    return(video_url_list)


#针对视频的请求地址获取数据并对视频本地化存储
def get_vd(url):
    # for i in url:
    #     file_name=i.split('/')[6]
    #     print(file_name)
    #     response=session.get(url=i,headers=headers)
    #     page_text=response.content
    #     #print(page_text)
    #     with open(f'./{file_name}','wb') as f:
    #         f.write(page_text)
    file_name = url.split('/')[6]
    #print(file_name)
    print('正在下载' + file_name)
    response=session.get(url=url,headers=headers)
    page_text=response.content
    #print(page_text)
    with open(f'./{file_name}','wb') as f:
        f.write(page_text)
    print('下载完成' + file_name)


#开启线程池对多个视频进行同时爬取
def pool(url):
    #get_vd(url,session,headers)
    start_time=time.time()
    # 实例化一个线程池对象
    pool = threadPool(4)
    # 将列表中每一个列表元素传递给get_page进行处理
    pool.map(get_vd, url)
    end_time = time.time()
    pool.close()
    pool.join()
    print(f'耗时{end_time - start_time}')

#主程序
def main():
    # 获取生活页面中最热视频的各个链接地址
    rm_url=get_sh_detail(url_sh)
    # 针对各个链接地址中视频的src信息拿到视频的请求地址
    mp4_url=get_rm_detail(rm_url)
    #开启线程池对多个视频进行同时爬取
    #针对视频的请求地址获取数据并对视频本地化存储
    #get_vd(mp4_url, session, headers)
    pool(mp4_url)

if __name__ == '__main__':
    main()