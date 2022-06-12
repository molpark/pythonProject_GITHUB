# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 11:47
# @Author  : lys
# @Project : pythonProject
# @File    : 正则表达式.py
import re
#正则表达式 字符串相关 重在处理规则
#python字符串中是否包含p
#普通字符
res=re.findall('p','python')
res=re.findall('python','i like python')
res=re.findall('o','i like python')
res=re.findall('2','123456abcdef')

#预定义字符
'''
\d  匹配所有数字 ,[0-9]
\s 空白符,制表符,换行符
\w 包含下划线在内的字符a-zA-Z0-9_
\D 匹配所有非数字 ^\d
\S 取反空白符,制表符,换行符
\W 包含非正常字符,特殊字符
'''
res=re.findall(r'\d','123456ab_cdef$#@')
res=re.findall(r'\D','123456ab_cdef$#@')
res=re.findall(r'\w','123456ab_cdef$#@')
res=re.findall(r'\W','12 345\t6a\nb_cdef$#@')
res=re.findall(r'\s','12 345\t6a\nb_cdef$#@')
res=re.findall(r'\S','12 345\t6a\nb_cdef$#@')

#findall匹配所有满足条件的正则
#元字符
'''
[] 匹配一个字符,括号内的字符是或者的关系
^  取反  \D =^\d
-  区间
'''
res=re.findall(r'[678a]','12 345\t6a\nb_cdef$#@')
res=re.findall(r'[\d\s]','12 345\t6a\nb_cdef$#@')
res=re.findall(r'[^\d\s]','12 345\t6a\nb_cdef$#@')
res=re.findall(r'[1-4]','12 345\t6a\nb_cdef$#@')
res=re.findall(r'[a-d]','12 345\t6a\nb_cdef$#@')
res=re.findall(r'[1-4a-d_%\s]','12 345\t6a\nb_cdef$#@')

#() 分组
res=re.findall(r'a[abc]','aaabacad')
res=re.findall(r'a([abc])','aaabacad')#还没讲具体规则

#重复匹配
'''
{n}表示前面的字符重复n次
{n,m}表示前面的字符至少出现n次,最多出现m次
{n,}表示前面的字符出现n次到任意次,多大都可以
'''
res=re.findall(r'\d\d\d','12 345\t6a\nb_cdef$#@')
res=re.findall(r'\d{3}','12 345\t6a\nb_cdef$#@')
#贪婪匹配尽量匹配更多的字符以最大的3为标准
res=re.findall(r'\d{1,3}','12 345\t6a\nb_cdef$#@')
#非贪婪匹配以最小的1为标准(好像没啥意义,都是按照最小的取,和{n}一样)
res=re.findall(r'\w{2,3}?','12 345\t6a\nb_cdef$#@')
res=re.findall(r'\w{2,}','12 345\t6a\nb_cdef$#@')
'''
? 表示前面的字符出现0次或1次 {0,1}
+ 表示前面的字符出现至少一次 {1,}
* 表示前面的字符出现0次或任意次
'''
res=re.findall(r'\d?','12 345\t6a\nb_cdef$#@')
res=re.findall(r'\w?','12 345\t6a\nb_cdef$#@')
res=re.findall(r'\w+','12 345\t6a\nb_cdef$#@')
res=re.findall(r'\w+?','12 345\t6a\nb_cdef$#@')
res=re.findall(r'\w*','12 345\t6a\nb_cdef$#@')
'''
转义符  \d * +
'''
res=re.findall(r'\\d','12 345\t6a\nb_cdef$#@\d')
res=re.findall(r'd\*+','12 345\t6a\nb_cdef$#@\d***')
res=re.findall(r'\w+\+b','12 345\t6aa+b\nb_cdef$#@\d***')

'''
贪婪和非贪婪
最大的应用场景:爬虫
'''
res=re.findall(r'd\w+d','dxxxxxxxxdxxxxxxd')
res=re.findall(r'd\w+?d','dxxxxxxxxdxxxxxxd')

#非贪婪的案例
# .属于除了换行符这些的其他字符
#提取td括起来的内容
htmlstr='''
<td>python</td><td>$123</td><td>12343@11.com</td>
'''
res=re.findall(r"<td>(.+?)</td>",htmlstr)


'''
反向引用
'''
#找出前后引号一致的数据
#\1代表了第一个分组,向前引用.(反向引用)
wordstr="""
'hello' "python" 'love" "haha'
"""
res=re.findall(r"('|\")(\w+)(\1)",wordstr)
#print(res)
#print([x[1] for x in res])

#校验密码 122223 111222 121212 123321
res=re.findall(r"(\d)(\1{2,})",'122223')
res=re.findall(r"(\d)(\1{2,})",'111222')
#print([x[0]+x[1] for x in res])


#位置匹配
res=re.findall(r"\d{11}",'13717890407')
res=re.findall(r"\d{11}",'1371789040712312412')
#^ $    ^代表开头 $代表结尾   $带上意味着要把后面字符串全部拿进来匹配
res=re.findall(r"^\d{11}$",'1371789040712312412')
res=re.findall(r"^\d{11}$",'13717890407')
print(res)