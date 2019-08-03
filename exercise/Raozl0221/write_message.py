#encoding:utf-8
filename = '..\\text_files\\test.txt'

with open(filename,'a') as file_object:
    file_object.write("尼玛的狗.")
with open(filename, 'r') as file_object:
    for line in file_object:
        print(line.rstrip())