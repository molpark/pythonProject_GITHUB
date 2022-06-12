import pandas as pd
fpath=r'C:\job\learning\pythonProject\venv\learn\Pandas\file\新建文本文档.txt'

n=pd.read_csv(fpath,sep='\t')
#print(n)

###案例
m=pd.read_csv(fpath,      ##路径
              sep='\t',    ##指定分隔符
              header=None,  ##这个文件没有标题行,不需要标题行
              names=['pdate','pv'], ##指定列名
              encoding='utf-8'     ##指定编码格式
              )
print(m)