#一个接口多个形态,表现的形态不一样

#一个简单的多态形式,一般不用这种写法来写
class Dog:
    def sound(self):
        print('汪汪汪')
class Cat:
    def sound(self):
        print('喵喵喵')
def animal_sound(obj):
    '''统一调用接口,不管你传进来的是什么动物,我都调用sound方法'''
    obj.sound()

d=Dog()
animal_sound(d)
c=Cat()
animal_sound(c)

##常用的写法
