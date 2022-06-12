def dog(name, d_type):  # 模板
    data = {'name': name,
            'd_type': d_type,
            'life_val': 100
            }
    attack_val = {
        'jingba': 30,
        'zangao': 40
    }
    if d_type in attack_val:
        data['attack_val'] = attack_val.get(d_type)
    else:
        data['attack_val'] = 15

    def dog_bite(person_obj):
        person_obj['life_val'] -= data['attack_val']
        print(f"狗{data['name']}要了{person_obj['name']}一口,还有血量{person_obj['life_val']}")
        print("狗%s咬了%s一口,还有血量%s" % (data['name'], person_obj['name'], person_obj['life_val']))

    data['bite'] = dog_bite # 为了从函数外部可以调用 DOG_BITE方法
    return data

def person(name, age):
    data = {
        'name': name,
        'age': age,
        'life_val': 100
    }
    if age > 18:
        data['attack_val'] = 80
    else:
        data['attack_val'] = 60
    return data


a = dog('jjj', 'zangao')  # 实体
b = dog('ccc', 'jingba')
c = dog('ddd', 'xiaohua')
d = person('xiaoming', 30)
print(a, b, c, d)

#调用函数内部的方法.此步是为了bite 的方法只属于狗.不能属于人
a['bite'](d)
