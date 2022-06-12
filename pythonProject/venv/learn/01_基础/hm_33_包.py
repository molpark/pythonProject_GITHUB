"""
包
概念
    1.包是一个包含多个模块的特殊目录
    2.目录下有一个特殊的文件__init__.py
    3.包名的命名方式和变量名一致,小写字母
好处:使用import包名 可以一次性导入包中的所有模块

__init__.py
要在外界使用包中的模块,需要在__init__.py中指定对外界提供的额模块列表
from . import send_message
from . import receive_message
"""

import hm_message
hm_message.send_message.send("xiaoming")
n=hm_message.receive_message.receive()
print(n)