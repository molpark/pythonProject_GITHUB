'''
封装

'''

class Person:
    def __init__(self,name,age):
        self.name=name  #实例变量,成员变量,公有属性
        self.age=age
        self.__life_val=100  #私有变量,私有属性 在变量前两个下划线
        '''好处是无法在外面获取并且修改值.
        可以通过一个方法获取,并且作为范围.现在就只可以获取这个但是无法修改这个私有属性'''
    def get_life_val(self):
        print(self.__life_val)
        self.__breath()   ##调用私有方法
    def get_attack(self):   #要修改私有属性也需要在类里面写方法去修改
        self.__life_val-=20
    def __breath(self):   #方法也可以作为私有方法.
        print(f'{self.name} is breathing')


p=Person('alex',12)
#print(p.__life_val)  #外部就无法访问这个私有属性,只能在类里面进行使用
p.get_attack()
p.get_life_val()


###访问内部私有方法和属性,一般不推荐这么用,私有方法就是为了封装好用的.并且还能修改属性值
#实例名._类名方法名
p._Person__breath()
p._Person__life_val=10  #修改私有属性
p.get_life_val()

##实例生成后再创建的私有属性,并不具有私有性,是可以直接访问的
p.__val=400
print(p.__val)