##循环体关键字break,comtinue
#break 退出循环体

i=0
while i<10:
    #break 某一条件满足时,退出循环,不再执行后续重复命令
    #假定i==7退出循环
    print(i)
    if i==7:
        break
    i+=1
    print("到",i)
print("bububu")

###continue 某一条件满足时,跳过continue后的执行语句重新进入循环判断啊
i=0
while i<10:
    if i==3:
        #注意:在循环中使用continue之前
        #需要确认循环计数的修改是否会被修改,否则死循环
        i += 1
        continue
    print(i)
    i += 1
print(i)


###