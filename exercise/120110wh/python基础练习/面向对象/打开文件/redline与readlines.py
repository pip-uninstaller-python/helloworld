import pprint
# 打开文件
file_name = 'hello\\logFile.tet'

with open(file_name,encoding="utf-8") as file_obj:
    # readline()
    # 该方法可以用来读取一行内容
    #print(file_obj.readline())
    #print(file_obj.readline())
    #print(file_obj.readline())
    #print(file_obj.readline(),end="")
    # readlines()
    #该方法用于一行一行的读取内容，它会一次性将读取到的内容封装到一个列表中返回
    #r = file_obj.readlines()
    #pprint.pprint(r)

    for t in file_obj:
        print(t)