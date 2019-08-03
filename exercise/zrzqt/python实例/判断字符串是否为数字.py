def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False
#测试字符串和数字
print(is_number('foo'))#False
print(is_number('1'))#True
print(is_number('1.3'))#True
print(is_number('-1.37'))#True
print(is_number('1e3'))#True
#测试 Unicode
print(is_number('四'))#True
#通过创建自定义函数is_number()方法来判断字符串是否为数字
