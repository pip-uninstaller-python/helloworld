#教程代码当出现多个汉字数字时会报错，通过遍历字符串来解决
#对汉字表示的数字也可分辨
def is_number(s):
    try:#如果能运行float(s)语句，返回True(字符串s是浮点数)
        float(s)
        return True
    except ValueError:#ValueError为python的一种标准异常，表示转入'无效的参数'
        pass#如果引发了ValueError这种异常，不做任何事情(pass,不做任何事情，一般做占位语句)
    try:
        import unicodedata #处理ASCII码的包
        for i in s:
            unicodedata.numeric(i)#把一个表示数字的字符串转换为浮点数返回的函数
            return True
        return True
    except (TypeError,ValueError):
        pass
    return False
