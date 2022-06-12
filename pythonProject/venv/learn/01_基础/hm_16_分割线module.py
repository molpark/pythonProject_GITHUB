def print_line(eng,num):
     print(eng*num)



def print_line_times(times, num, eng):
    """打印单行分割线(光标移动到函数名点击小灯泡)
    :param times:
    :param num:
    :param eng:
    """
    i = 0
    while i <= times:
        print_line(eng, num)
        i += 1
name="luyishun"