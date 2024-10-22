# 打开文件
file_name = 'hello\\logFile.tet'
# 调用open()来打开文件
file_obj = open(file_name)

# 当我们获取了文件对象以后，所有的对文件的操作都应该通过对象来进行
# 读取文件中的内容
# read()读取文件
content = file_obj.read()

print(content)

# 关闭文件
# 调用close()方法来关闭文件
file_obj.close()

# 关闭文件的另一种方法
# with ... as 语句，
#with open(file_name) as file_obj :
    # 在with语句中可以直接使用file_obj来做文件操作
    # 此时这个文件智能在with中使用，一旦with结束则文件会自动close()
    #print(file_obj.read())
file_name = "demo.tet"

try:
    with open(file_name) as file_obj :
        print(file_obj.read())
except FileNotFoundError:
    print(f"{file_name}文件不存在")