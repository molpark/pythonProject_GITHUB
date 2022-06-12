#!/usr/bin/env python
# encoding: utf-8
'''
@author: luyishun
@file: 图片压缩.py
@time: 2022/6/9 19:21
@desc:
'''
import PIL
from PIL import Image
from tkinter.filedialog import *
#自己筛选图片文件
fl=askopenfilenames()
img = Image.open(fl[0])
img.save("result.jpg", "JPEG", optimize = True, quality = 10)