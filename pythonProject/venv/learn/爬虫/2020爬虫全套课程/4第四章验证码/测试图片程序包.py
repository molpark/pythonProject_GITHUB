# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 17:23
# @Author  : lys
# @Project : pythonProject
# @File    : 测试图片程序包.py

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\software\Tesseract-OCR\tesseract.exe"

def demo(img_path):
    # 打开要识别的图片
    image = Image.open(img_path)
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    text = pytesseract.image_to_string(image, lang='chi_sim')

    # 输入所识别的文字
    print(text)


if __name__ == '__main__':
    demo('./img.png')
