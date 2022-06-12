class Base(object):
    def eat_peach(self):
        print('&&&在吃桃子')


class ShenXianBase(Base):
    def eat_peach(self):
        print('老神仙在吃桃子')

class ShenXian(ShenXianBase):
    def fly(self):
        print('神仙飞')
    def eat_peach(self):   #有继承顺序,从左到右(在继承的时候的顺序)
        print('神仙吃桃子')

class MonkeyBase(Base):    #一个看继承顺序另外看能在上一层找到了就不会再往上上层找了,先是深度优先找(先从下往上找),找不到再是广度优先找
    pass
    # def eat_peach(self):
    #     print('老猴子在吃桃子')


class Monkey(MonkeyBase):
    pass
    # def eat_peach(self):
    #     print('猴子吃桃')

class Sun(Monkey,ShenXian):
    def jingubang(self):
        print('耍棒子')

#还可以继承的再继承多代继承
class xiaohouzi(Sun):
    def chifan(self):
        print('吃饭')

m1=Sun()
m1.eat_peach()
m1.fly()
m1.jingubang()

m2=xiaohouzi()
m2.eat_peach()




class A:   #经典类 采用的都是深度优先
    pass
class B(object): #新式类 采用的都是广度优先
    pass
'''为什么说广度优先.是因为如果底层的两个类最终都指向最上方同一个类,那么就是广度优先,一般是网上找找到最上面那个原始类之前都没有找到的话,那就会换条路找
            1
         2     3
       4         5
       广度优先的查找顺序是 42531  就要在最上面那个类中定义的时候带上(object)
       深度优先的殊勋是421,531

   如果不是指向同一个类那就是通过深度来差搜找
'''

'''
多继承C3算法
python3 默认都是新式类.
'''

