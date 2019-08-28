# 文件（File）
#   -通过Python程序来对计算机中的各种文件进行增删减改查的操作
#   -I/O（Input/Output）
file_name = "hello\\logFile.tet"
# 在windows系统使用路径时，可以使用/来代替\
# 或者可以使用\\来代替\
# 或者也可以使用原始字符串r"XXXX"
# <_io.TextIOWrapper name='hello\\logFile.tet' mode='r' encoding='cp936'>
# <_io.TextIOWrapper name='hello/logFile.tet' mode='r' encoding='cp936'>
print(open(file_name))

# 表示路径，可以使用..来返回一级目录
# 如果目标文件距离当前文件比较员，此时可以使用绝对路径
# 绝对路径应该从磁盘的根目录开始书写
file_name1 =  r"C:\\Users\\11466\\Desktop\\name.txt"
print(open(file_name1))