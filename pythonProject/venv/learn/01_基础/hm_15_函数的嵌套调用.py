def test1():
    print("步骤1")


def test2():
    test1()
    print("步骤2")

test2()

######演练1

def print_line(eng,num):

    print(eng*num)

print_line("abc",10)

def print_line_times(times,num,eng):
    """打印单行分割线(光标移动到函数名点击小灯泡)
    :param times:
    :param num:
    :param eng:
    """
    i=0
    while i<=times:
        print_line(eng,num)
        i+=1

print_line_times(5,10,"abcdefg")