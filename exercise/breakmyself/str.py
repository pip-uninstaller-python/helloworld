# -*- coding: utf-8 -*-
# 开发团队   ：pip uninstall python
# 开发人员   ：breakmyself
# 开发时间   ：2019/8/19  16:05 
# 文件名称   ：str.PY
# 开发工具   ：PyCharm
#github主页：https://github.com/breakmyself
"""
字符串和转移字符
"""
str1 = 'Charlie'
str2 = "疯狂软件教育"
print(str1)
print(str2)
#转义符  ' str3 = 'I'm a coder' 这样 写不正确，因为包含转义符 ' 需要使用 ""
#使用 “” python会将单引号当成字符串中的内容来操作
str3 = "I'm a coder"
print(str3)
str4 = '"Spring is here , let us jam!",said woodchuck.'
print(str4)
#python 运行使用转义字符，使用反斜线 \ 将字符串中的特殊字符进行转义，
#使用场景：在有单引号和双引号的情况下，必须使用转义字符
str5 = '"we are scared, Let\'s hide in the shade",sys the bird'
print(str5)
#字符串拼接
s1 = "Hello, Charlie"
print(s1)
s2 = "人生苦短 "
s3 = " 我用Python"
s4 = s2 + s3
print(s4)
#repr和字符串：将字符串和数值进行拼接时候可以使用repr
s1 = "这本书的价格是："
p = 99.8
#直接打印价格会报错，python不允许字符串和数值直接拼接
#print(s1+p)
print(s1+str(p))
#或者使用 repr将数值转换成字符串
print(s1+repr(p))
#str()和 repr()都可以将数值转换成字符串，str是python的内置函数，repr是一个函数
st = "I will play my fife"
print(st)
print(repr(st))
#I will play my fife
#'I will play my fife'

