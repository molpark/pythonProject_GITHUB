import pandas as pd
import json


data = [{
    'name': 'pengjunlee',
    'age': 32,
    'vip': True,
    'address': {'province': 'GuangDong', 'city': 'ShenZhen'}
}
    ,{
    'name': 'xiali',
    'age': 18,
    'vip': False,
    'address': {'province': 'shanhahi', 'city': 'shanghai'}
    }]
#print(data)
ac=[]
for i in data:
    name=i.get("name",'')
    province=i["address"].get("city",'')
    ac= [name,province]
    print(ac)
    column=['name','city']
    print(column)
    #test=pd.DataFrame(columns=column,data=ac)

#test.to_csv('D:/test.csv')
