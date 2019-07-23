file = open('test1.txt')#打开test1文件
a = file.read()#使用read方法读取
file.close()#关闭
file = open('test2.txt')#打开test2文件
b = file.read()#使用read方法读取
file.close()#关闭
file = open('test3.txt', 'w')#打开test3文件,并只允许写数据
l = a + b #test1的文件内容与tset2的文件内容整合
file.write(l)#写入test3文件
file.close()#关闭
