# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 17:23
# @Author  : lys
# @Project : pythonProject
# @File    : 测试图片程序包.py
'''
支持的语言
    #['chi_sim', 'chi_sim_vert', 'eng', 'osd']
    chi_sim 文字按行 ,chi_sim_vert文字按列, eng 英语 osd
    print(pytesseract.get_languages(config=''))
数字不需要设置
lang='chi_sim+eng' #是可以混搭的
config = r'-l chi_sim+eng --psm 6' 也可以用次方法设置语言 和上面chi_sim+eng一样
config = r'--oem 3 --psm 6 outputbase digits' 只要数字
'''

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\software\Tesseract-OCR\tesseract.exe"

def demo_cn(img_path):
    # 打开要识别的图片
    image = Image.open(img_path)
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    #lang='eng'设置为英语
    text = pytesseract.image_to_string(image, lang='chi_sim', config='--psm 6') \
        .replace('‘', '').replace(',', '').replace('-', '').replace(':', '').replace('.', '')
    # 输入所识别的文字
    return text

def demo_all(img_path):
    # 打开要识别的图片
    image = Image.open(img_path)
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    text = pytesseract.image_to_string(image,lang='chi_sim+eng', config='--psm 6')\
        .replace('‘', '').replace(',', '').replace('-', '').replace(':', '').replace('.', '')
    # 输入所识别的文字
    return text

def demo_eng(img_path):
    # 打开要识别的图片
    image = Image.open(img_path)
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    text = pytesseract.image_to_string(image,lang='eng', config='--psm 6')\
        .replace('‘', '').replace(',', '').replace('-', '').replace(':', '').replace('.', '')
    # 输入所识别的文字
    return text



def demo_only_num(img_path):
    #只提取数字
    # 打开要识别的图片
    image = Image.open(img_path)
    config = r'--oem 3 --psm 6 outputbase digits'
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    text = pytesseract.image_to_string(image, config=config)
    # 输入所识别的文字
    print(text)

if __name__ == '__main__':
    demo_all('./ccc.png')
