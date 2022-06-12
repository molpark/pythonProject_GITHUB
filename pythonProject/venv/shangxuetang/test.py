def list_dic(list1,list2):
    dic=dict(map(lambda x,y:[x,y],list1,list2))
    return dic


if __name__ == '__main__':
    print(list_dic(a,b))

a="lisi"
b=[]
b.append(a)
print(b)


dica={"zhangsan":300
      ,"lisi":400}
c=0
for i in dica.values():
    print(i)
    i=int(i)
    c=c+i
print(c)