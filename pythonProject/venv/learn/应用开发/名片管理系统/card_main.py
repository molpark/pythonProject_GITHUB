#!/usr/bin/python3

import card_tool

print("欢迎界面")
#无限循环
while True:
    # TODO(lys) 显示菜单  ##好像没效果
    card_tool.show_menu()
    action_str=input("请选择要执行的操作: ")
    print("你选择的操作是%s"%action_str)

    if  action_str in ["1","2","3"]:
        # 如果123是针对名片的操作
        #pass如果不想现在加入代码,可以使用pass关键字
        #表示占位符,能保证代码结构正确,pass关键字不会执行任何操作
        if action_str=="1":
            card_tool.new_card()
        elif action_str=="2":
            card_tool.show_all()
        elif action_str=="3":
            card_tool.search_card()
    elif action_str=="0":
        # 0退出系统
        print("退出")
        break
    else:
        # 其他内容输出操作错误
        print("操作错误")


