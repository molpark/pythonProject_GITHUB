# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 22:44
# @Author  : lys
# @Project : pythonProject
# @File    : 06.request实战之药监总局相关数据爬取.py  网站地址目前是加密,目前计数无法解析
import json
import requests
if __name__ == '__main__':
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5t.2ewpEllfEAwaRpeDKv_6mfqmYiI.4JfdNtNY.xy6WCYPpAaFG_oUYk4O1nFhJL7cNYaKw1OR73I5Qj0n8KH.8EnGRq.GSTZy_xuExjrlilx97.CAkyQvoWDqZFk7xJZRtCOTEFKdHhEBH9mGVzEWJg6JYs30.mCvPwpn04cOJkh7NQ6.P2.GYBkJ8xcssQleruZzE9veai3fGVCdzhlmnnMfqSpM600_4pe8cq3QicP10pro_aBgQThmgqDsexVqocDXoqHZcaWjhn7NuKRPS6Kk1INpznBPDQnfOVNi9&8X7Yi61c=4Z6UNGniv_sop7kqr5F.Gm9L1hfb2mXNT73eD8zU2vNI.4BBAjHbxUrQ0jLNvPoNKZjvcBxXrWcoVjhbySUbPeL6hH2M2_p8rEWywiEPyQV0ocEixP7wEalzs36DCbAXO'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    data={
'on':' true',
'page':' 1',
'pageSize':' 15',
'productName':'',
'conditionType':' 1',
'applyname':'',
'applysn':''
    }
    id_list=[]
    response=requests.post(url=url,headers=headers,data=data).json()
    data_id=response.get('list')
    for id in data_id:
        id_list.append(id.get('ID'))


##下次看数据解析概述 p16