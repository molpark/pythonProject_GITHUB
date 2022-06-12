#类的组合关系
#由一堆组件构成一个完整的实体,组件本身独立,但又不能自己运行,必须由宿主组合在一起才能运行
#类与类之间的互相调用

class Dog:
    d_life=100
    def __init__(self,name,age,attack):
        self.name=name
        self.age=age
        self.attack=attack
    def bite(self,pers):
        pers.p_life-=self.attack
        print(f'狗{self.name}咬了{pers.name}一口,还剩血量{pers.p_life}')


class Person:
    p_life=1000
    def __init__(self,name,age,attack):
        self.name=name
        self.age=age
        self.attack=attack
        self.weapon=Weapon()   ##直接实例化
    def hit(self,shad):
        shad.d_life-=self.attack
        print(f'人{self.name}打了狗{shad.name},还剩血量{shad.d_life}')


class Weapon:
    def dog_stick(self,obj):
        """打狗棒"""
        self.name='打狗棒'
        self.attack_val=40
        obj.d_life-=self.attack_val
        self.print_log(obj)
    def print_log(self,obj):
        print(f"{obj.name}被{self.name}打了还剩血量{obj.d_life}")

d1=Dog('傻狗',12,20)
p1=Person('傻蛋',32,40)
p1.weapon.dog_stick(d1)
