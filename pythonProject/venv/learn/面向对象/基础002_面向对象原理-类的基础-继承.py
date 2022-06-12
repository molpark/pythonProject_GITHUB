##两个子类继承了一个父类


#父类可以有共用的属性和方法.
class Animal:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print(f"{self.name} is eating")

#子类可以再单独写自己独有的方法和属性,并且可以重构父类的方法和属性
class Person(Animal):  ##定义类的时候带上() 里面写上其他类的名称,就代表了继承了那个类的功能
    #如果在子类里面重构了初始化属性,那么在调用的时候只需要传name的值就行了.这时候只认子类的初始化属性
    #初始化属性也可以做父类的延伸
    def __init__(self,name,age,sex,hobbie):
        #Animal.__init__(self,name,age,sex)    #子类的属性和父类的属性进行了绑定(延伸用)
        #super(Person,self).__init__(name,age,sex) #python3常用的方法,子类属性和父类的进行绑定(语法效果同上)
        super().__init__(name, age, sex)  # python3常用的方法,子类属性和父类的进行绑定(语法效果同上)(这种写法更加简单点)
        self.hobbie=hobbie

    def talk(self):
        print(f'{self.name}is talking')
    def eat(self):
        #这种属于父类的也用.子类再做一定的延伸.还要用父类的情况的下可以调用父类的方法.也可以不需要调用.完全重写父类方法
        #Animal.eat(self) #执行父类的方法 单继承,说明只继承Animal的eat 方法
        super().eat()  #执行父类的方法(写法更简单更常用)  可以额外使用在多继承中.
        print(f'{self.name}吃的很香')

class Dog(Animal):
    def chase(self):
        print(f'{self.name} is chasing')

if __name__ == '__main__':
    p=Person('mjj',12,'M','女人')
    p.eat()
    p.talk()
    d=Dog('xiaohuang',2,'M')
    d.eat()
    d.chase()
    print(p.sex,p.hobbie)