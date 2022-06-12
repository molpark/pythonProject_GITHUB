import json
data = {
    'name': 'pengjunlee',
    'age': 32,
    'vip': True,
    'address': {'province': 'GuangDong', 'city': 'ShenZhen'}
}

data_line=json.dumps(data)

data_ac=json.loads(data_line)

text=data_ac.get('name')



#print(i)
#print(data_ac.get(i))
name=data_ac.get("name")
age=data_ac.get("age")
vip=data_ac.get("vip")
province=data_ac.get("address").get("province")
city=data_ac.get("address").get("city")
fg='\t'
sti=name+fg\
     +str(age)+fg
print(sti)
