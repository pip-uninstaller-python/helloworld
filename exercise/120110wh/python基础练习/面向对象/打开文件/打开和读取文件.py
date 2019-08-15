# 打开文件
file_name = 'hello\\logFile.tet'

try:
    # 调用open()来打开一个文件，可以将文件分成两种类型
    # 一种时纯文本文件(使用UTF-8灯编码编写文本文件)
    # 一种是二进制文件(图片，MP3，ppt灯这些文件)
    # open()打开文件时，默认是以文本的类型打开的，但是open()默认的编码为None
    # 所以处理文本文件时必须要指定文件的编码(encoding='utf-8')
    with open(file_name,encoding='utf8') as file_obj :
        # 通过read()来读取文件中的内容
        # 如果直接调用read()他会将文本文件的所有内同全部读取出来
        #   如果要读取的文件较大的话，会一次性将文件的内同加载到内存中，容易导致内存泄漏
        #   所以对于较大的文件们不要直接调用read()
        # read()可以接收一个size作为参数，该参数用来指定读取的字符数量
        #   默认值为-1，他会读取文件中的所有字符

        content = file_obj.read()
        print(content)
except FileNotFoundError:
    print(f"{file_name}不存在~~~~")

# 读取大文件的方式
# 打开文件
file_name = 'hello\\logFile.tet'

try:

    with open(file_name,encoding='utf8') as file_obj:
        # 定义一个变量来保存文件的内容
        file_content = ""
        # 定义一个变量，来指定每次读取的大小
        chunk = 100
        # 创建一个循环来读取文件的内容
        while(1):
            # 读取chunk大小的内容
            content = file_obj.read(chunk)
            # 检查是否读取到了内容
            if not content :
                # 内容读取完毕
                break
            else:
                #print(content,end="")
                file_content += content

except FileNotFoundError:
    print(f"{file_name}不存在~~~~")


print(file_content)