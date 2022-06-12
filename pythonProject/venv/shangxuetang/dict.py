excel=[{"name":"xiaoyi"
        ,"age":18}
       ,{"name":"xiaoli"
        ,"age":17}
       ,{"name":"xiaolu"
        ,"age":16}
       ]
print(excel)

print(excel[2].get("name"))

for i in excel:
    a=i.items()
    b=list(a)
    print(b[0][0])
