# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 20:51
# @Author  : lys
# @Project : pythonProject
# @File    : test_001_client.py

import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print(s.recv(1024))


