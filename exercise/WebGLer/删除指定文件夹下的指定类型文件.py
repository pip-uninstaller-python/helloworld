import os
set_dir = "d:\\"        #设置指定文件夹
for i in os.listdir(set_dir):
    # print(i)
    if i.endswith('.txt'):      #删除set_dir文件夹下以.txt文件结尾的文件
        file_dir = set_dir + i
        # print(i)
        os.unlink(file_dir)
