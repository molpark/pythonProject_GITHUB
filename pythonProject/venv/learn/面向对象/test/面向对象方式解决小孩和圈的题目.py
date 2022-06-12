# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 15:18
# @Author  : lys
# @Project : pythonProject
# @File    : 面向过程方式解决小孩和圈的题目.py

#d第一类小孩,第二类圈
#小孩属性:编号,左手,右手
#圈属性:头和尾 行为:加一个小孩,移除一个小孩
class Kid:
    def __init__(self,gid):
        self.gid=gid
        self.left=None
        self.right=None

class Cycle:
    def __init__(self,count):
        self.head=None
        self.tail=None
        for i in range(count):
            self.add(Kid(i+1))

    def add(self,kid):
        '''向圈中增加一个小孩'''
        if self.head is None and self.tail is None:
            self.head=kid
            self.tail=kid
            kid.left=kid
            kid.right=kid
        else:
            kid.left=self.head
            kid.right=self.tail
            self.head.right=kid
            self.tail.left=kid
            self.tail=kid

    def remove(self,kid):
        '''从圈中移除小孩'''
        if kid is self.head:
            self.head=kid.left
        if kid is self.tail:
            self.tail=kid.right
        kid.left.right=kid.right
        kid.right.left=kid.left
        kid.left=None
        kid.right=None

cycle=Cycle(500)
cur=cycle.head
step=1
while cycle.head is not cycle.tail:
    cur=cur.left
    if step%3==0:
        cycle.remove(cur.right)
    step+=1
print(cycle.head.gid)