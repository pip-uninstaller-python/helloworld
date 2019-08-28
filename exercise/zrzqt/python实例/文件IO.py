#python中文件相关操作，包括open read write
#写文件
with open('text.txt','wt')as out_file:
    out_file.write('以下内容将会写入文本\n写入成功！')
#read a file
with open('text.txt','rt')as in_file:
    text = in_file.read()
print(text)
#此实例会在本文件相同位置创建text.txt
