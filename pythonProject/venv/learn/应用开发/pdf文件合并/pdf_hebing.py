# -*- coding: utf-8 -*-
# @Time    : 2022/5/15 14:36
# @Author  : lys
# @Project : pythonProject
# @File    : pdf_hebing.py

#参考资料 https://zhuanlan.zhihu.com/p/142541370
import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
path =r'C:\Users\卢一顺\Desktop\洪恩识字字帖'
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

#有四个文件需要放到列表后面 也可以手动更新列表为下面循环所用
for i in range(4):
    a=pdfFiles.pop(0)
    pdfFiles.append(a)
print(pdfFiles)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(os.path.join(path,filename), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages (except the first) and add them.
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('./allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()