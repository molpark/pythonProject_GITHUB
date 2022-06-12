# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 20:50
# @Author  : lys
# @Project : pythonProject
# @File    : test_001.py

# import socket
# s = socket.socket()
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
# s.listen(5)
# while True:
#  c, addr = s.accept()
#  print('Got connection from', addr)
# c.send('Thank you for connecting')
# c.close()


# from socketserver import TCPServer, StreamRequestHandler
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.request.getpeername()
#         print('Got connection from', addr)
#         self.wfile.write(b'Thank you for connecting')
# server = TCPServer(('', 1234), Handler)
# server.serve_forever()


# 代码清单14-4 分叉服务器  windows机器不支持
# from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler
# class Server(ForkingMixIn, TCPServer): pass
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.request.getpeername()
#         print('Got connection from', addr)
#         self.wfile.write(b'Thank you for connecting')
# server = Server(('', 1234), Handler)
# server.serve_forever()

# 代码清单14-5 线程化服务器
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
class Server(ThreadingMixIn, TCPServer): pass
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write(b'Thank you for connecting')
server = Server(('', 1234), Handler)
server.serve_forever()
