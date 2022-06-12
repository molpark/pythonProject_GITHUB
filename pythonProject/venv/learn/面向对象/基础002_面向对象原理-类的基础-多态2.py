
'''抽象的类实现多态的形式'''
class Document:
    def __init__(self,name):
        self.name=name
    def show(self):
        raise NotImplementedError('subclass must implement abstract method') ##抛出子类必须要重写父类的方法
class Pdf(Document):
    def show(self):
        print('show pdf')
class Word(Document):
    def show(self):
        print('show word')


p=Pdf('dsa')
w=Word('zzz')
for i in [p,w]:
    i.show()