# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 21:19
# @Author  : lys
# @Project : pythonProject
# @File    : json_test001.py

#此种方法只能解以下的json案例,和纯单层字典
#这种方法主要用于不知道key 是什么的时候

d1 = [{"id" : 1,"name" : "Number1","age" : 11},{"id" : 2,"name" : "Number2","age" : 22},{"id" : "3","name" : "Number3","age" : 33}]
d2 = {"persons" :[{"id" : 1,"name" : "Number1","age" : 11},{"id" : "2","name" : "Number2","age" : 22},{"id" : 3,"name" : "Number3","age" : 33}]}
d3 = {"code" : 200, "persons" :[{"id" : 1,"name" : "Number1","age" : 11},{"id" : True,"name" : "Number2","age" : 22},{"id" : 3,"name" : "Number3","age" : 33}]}
d4=[{'name':'xiaowang','age':20},{'name':'xiaolv','age':30}]

import pandas as pd

## 获取 json 数组或json 对象的 key 列表
def get_json_keys(json_str,json_keys = []):
    if isinstance(json_str,list):
        for json_obj in json_str:
            for key in json_obj.keys():
                if key not in json_keys:
                    json_keys.append(key)
    elif isinstance(json_str,dict):
        for key in json_str.keys():
                if key not in json_keys:
                    json_keys.append(key)
    return json_keys


## 将json 数组中相同的 key - value值进行合并

def get_key_values(json_str,json_keys):
    target_json = {}
    for key in json_keys:
        key_values = []
        for json_obj in json_str:
            if isinstance(json_obj,dict):
                key_values.append(json_obj[key])
        target_json[key] = key_values
    return target_json

## 主方法
def analyse_json(json_str):
    target_json = {}
    json_keys = []
    if isinstance(json_str,list):
        json_keys = get_json_keys(json_str,json_keys)
        target_json = get_key_values(json_str,json_keys)
    elif isinstance(json_str,dict):
        json_keys = get_json_keys(json_str,json_keys)
        for key in json_keys:
            if not isinstance(json_str[key],list) and not  isinstance(json_str[key],dict):
                target_json[key] = json_str[key]
            else:
                target_json[key] = analyse_json(json_str[key])
    return target_json

rows=analyse_json(d4)



file_name= '../test/json_test001file.txt'

dataf=pd.DataFrame(rows)
dataf=dataf.values.tolist()
# print(dataf)
for dad in dataf:
    #将其中的元素都转换成字符串
    dad=[str(x) for x in dad]
    print(dad)
    list_data = '\x1f'.join(dad)
    with open(file_name, 'a', encoding="utf-8") as f:
        f.write(list_data + '\n')
