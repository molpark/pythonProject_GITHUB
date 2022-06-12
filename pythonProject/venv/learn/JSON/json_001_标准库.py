# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 22:36
# @Author  : lys
# @Project : pythonProject
# @File    : json_001_标准库.py
import json
#从python 对象格式化一个 json string
#将python数据类型转换为json格式的字符串(dump string)
person ={'name':'sniper','age':30,'tel':['123213','325325'],'isonly':True}
person_json=json.dumps(person,indent=4,sort_keys=True) #json 格式化输出indent, sort_key 针对key 的字母排序
print(type(person))
print(type(person_json))
print(person)
print(person_json)


#将python数据类型转换并保存到json格式的文件内
json.dump(person,open('data.json','w'),indent=4)


#将json格式的字符串转换为python的类型(load string)
per=json.loads(person_json)
print(per)
print(type(per))
for i in per:
    print(per.get(i))

#从json格式的文件中读取数据并转换为python的类型
per_file=json.load(open('data.json','r'))
print(per_file)

