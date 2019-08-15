import time
file_name = "C:\\Users\\11466\\Desktop\\李琛-窗外.mp3"

# 读取模式
# t 读取文本文件(默认值)
# b 读取二进制文件
with open(file_name,"rb") as file_obj:

    new_name = "aa.flac"
    with open(new_name,"wb") as new_obj:
        # 定义每次读取的大小
        chunk = 1024*100
        while True:
            content = file_obj.read(chunk)
        # 将读取道德数据写入到新对象中
            if not content:
                break
            new_obj.write(content)
