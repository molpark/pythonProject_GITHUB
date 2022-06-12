#记录所有的名片字典
card_list=[]

def show_menu():
    """显示餐带"""
    print("*"*50)
    print("欢迎使用它")
    print("")
    print("1.新增文件")
    print("2.查看文件")
    print("3.搜索文件")
    print("0.退出系统")
    print("*" * 50)

def new_card():
    """新增名片"""
    print("*"*50)
    print("新增")
    name =input("请输入姓名")
    phone=input("请输入电话")
    qq=input("请输入qq")
    dict={"name":name,
          "phone":phone,
          "qq":qq}
    #将名片字典加入到列表中
    card_list.append(dict)
    print("添加%s成功"%name)

def show_all():
    """显示所有名片"""
    print("*" * 50)
    if card_list==[]:
    # if len(card_list)==0:
        print("名片记录为空,请新增名片")
        #return可以返回一个函数的执行结果
        #下方的代码不会执行
        #如果return后面没有任何内容,表示会返回到
        #调用函数的位置,并且不返回任何结果
        return
    for i in card_list:
        #列表不齐可以使用\t\t
        print(i["name"],end=" ") #不换行
        print(i["phone"],i["qq"])

def search_card():
    """搜索名片"""
    print("*" * 50)
    print("搜索名片")
    find_name_yy=input("请输入要查找的姓名:")
    for i in card_list:
        if i["name"] ==find_name_yy:
            print(i)
            print(i["name"])
            print(i["phone"])
            print(i["qq"])
            print("已找到退出查询")
            deal_card(i)
            #针对找到的姓名增加修改功能
            break
    else:
        print("没有找到%s"%find_name_yy)

def deal_card(i):
    print("开始修改")
    print(i)
    action_str=input("要修改的内容"
                     "[1]修改[2]删除[0]返回上级菜单")
    if action_str=="1":
        i["name"]=input_card_info(i["name"],"姓名")
        i["phone"] = input_card_info(i["phone"], "电话")
        i["qq"] = input_card_info(i["qq"], "QQ")

    elif action_str=='2':
        card_list.remove(i)
        print("删除成功")
    elif action_str=="0":
        pass

#增加注释方法将鼠标放在函数上点击小灯泡选insert
    """输入名片信息

    :param ivalue: 
    :param tips: 
    :return: 
    """
def input_card_info(ivalue,tips):
    #1.提示用户输入内容
    #2.如果输入了内容直接返回结果
    #3.如果没有输入内容,返回原有的值
    result=input(tips)
    if len(result)==0:
        return ivalue
    else:
        return result


