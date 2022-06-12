score = int(input("小明的成绩是"))
print(score)
if score<60:
    print("成绩不及格")
elif score>60 and score<100:
    print(("优秀,分数是{}").format(score))
else:
    print("满分")