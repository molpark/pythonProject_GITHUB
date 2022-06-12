gl_list=[6,4,9]


##sort的缺省
##将最常见的值可以设置为缺省参数
gl_list.sort()
print(gl_list)
gl_list.sort(reverse=True)
print(gl_list)

#只需要在定义函数时将变量赋值,该变量就拥有了缺省值
#提示:在指定缺省参数的默认值时,应该使用最常见的值作为默认值
def print_info(name,gender=True):
    """

    :param name:xingming
    :param gender:TRUE男生 False女生
    :return:
    """
    gender_text="男生"
    if not gender:
        gender_text="女生"
    print("%s 是 %s"%(name,gender_text))

print_info("lishi")
print_info("xiaomei",False)


print("-------------------------")
#所有带缺省参数的,缺省参数应该放在所有参数的末尾

def print_info1(name,title,gender=True):
    """

    :param title: 职位
    :param name:xingming
    :param gender:TRUE男生 False女生
    :return:
    """
    gender_text="男生"
    if not gender:
        gender_text="女生"
    print("%s 是 %s是%s"%(name,gender_text,title))


print_info1("lishi","shuaige")
print_info1("xiaomei","xiaoji",False)

