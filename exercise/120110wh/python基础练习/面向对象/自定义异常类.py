# 自定义异常对象
# finally为最终显示
# 也可以自定义异常类，只需要创建一个类继承Exception即可
class MyError(Exception):
    pass

def add(a,b):
    if a < 0 or b < 0:
        # raise用来向外部抛出异常，后面可以跟一个异常类，或异常类的实例
        # raise Exception
        # 抛出异常的目的，告诉调用者这里调用时出现问题，希望你自己处理一下
        raise Exception("两个参数中不能有负数")  # 手动抛出异常
    r = a+b
    return r


print(add(-123,456))
