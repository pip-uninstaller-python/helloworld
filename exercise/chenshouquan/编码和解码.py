#encode()编码、 decode()解码
#ascii
#gb2312   gbk
#unicode
#utf-8
#编码和解码方式要一致
#Python3中字符串的两种类型：bytes,str,str存贮unicode类型，bytes存储byte类型

#字符串（unicode）转bytr------编码
a="我爱北京天安门"
b=a.encode("utf-8")#转成字节码 

print(b) #b'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'

#bytr转字符串(unicode)------解码
c=b.decode("utf-8")

print(c)