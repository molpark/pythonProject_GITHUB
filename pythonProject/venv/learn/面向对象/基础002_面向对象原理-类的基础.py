##面向对象
'''
实例化,就是指用模板(class)生成的实体的过程
实力化生成的视图,就被称为对象或者实例
self 代表实例本身
'''
class Dog:
    d_type='京巴'  #属性,类属性,类变量   ,公共属性 所有实例共享 ,一般在最外层
    def __init__(self,name,age,master): #初始化方法,构造方法,构造函数,实例化时会自动执行,进行一些初始化工作.
        print('hhh',name,age)
        # 要想把name,age这两个值,真正的存到实例里,那就要把2个值跟实例绑定
        self.name=name #绑定参数值到实例d2.name=name  实例属性,对应外层的公共属性有区别, 每个实例独享
        self.age=age
        self.master=master
        self.sayhi()
    def sayhi(self):   ##方法 ,第一个参数必须是self, self代表实例本身
        print(f'我是{self.d_type}名字{self.name},年龄{self.age},主人是{self.master.name}')

# d=Dog('小花','12')  #生成了一个实例
# d2=Dog('小李','13') #生成了一个实例
# d.sayhi() #实例.方法
# d2.sayhi()
#print(d.d_type) #实例.属性

#类属性的调用
#print(Dog.d_type)
#print(d.d_type)
#实例属性的调用,实例属性只存在实例属性中.无法通过类来直接找到实例属性
#print(d.name)

class Person:
    nation='中'
    #有想用属性的情况可以把实例属性放到类属性中,节省操作,节省空间
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        print(self.name,self.age,self.sex,self.nation)
# Person.nation='美'
# p=Person('momo','12','女')
# p.nation='日' # 相当于 给p实例创建了一个新的实例属性
# print(p.name,p.nation)

'''
类与类之间的关系
依赖关系
关联关系
组合关系
聚合关系
继承关系 累的三大特性之一,子承父业

'''
#类之间的依赖关系
# p=Person('mjj',12,'M')
# d=Dog('xxx',2,p)

#类的关联关系
class RelationShip:
    '''保存couple之间对象的关系'''
    def __init__(self):
        self.couple=[]
    def make_couple(self,obj1,obj2):
        self.couple=[obj1,obj2] # 两个人成了一个对象,将两个对象存在一个对象这
        print(f'{obj1.name}和{obj2.name}')
    def get_my_partern(self,relation):
        for i in self.couple:
            if i.name != relation.name:
                print(f'{relation.name}找{i.name}')

class Person1:
    def __init__(self,name,age,sex,relation):
        self.name=name
        self.age=age
        self.sex=sex
        #self.parter=None #应该是另一半,一个类无法上来就赋值,只好先给None 生成对象后再给这个属性赋值
        self.relation=relation
    def do_private_stuff(self,ooo):
        print(f'{self.name}喜欢{ooo.name}的***')

cou=RelationShip()
p1=Person1('xiaoming',12,'M',cou)
p2=Person1('xiaohua',8,'F',cou)
cou.make_couple(p1,p2)
#cou.get_my_partern(cou.couple)
p1.relation.get_my_partern(p1)
p1.do_private_stuff(cou.couple[1])


# #双向绑定(土办法,参考上面用的方法)
# p1.parter=p2
# p2.parter=p1
# p1.do_private_stuff()
# #删除关联关系
# p2.parter=None