# del函数的使用
a = [10,20,30]
print(a)
print(id(a))
del a[2]
print(a)
print(id(a))

#可以看到在删除前后a的地址没有变化

#pop方法的使
print("初始化为：b = [10,20,30,40,50]")
b = [10,20,30,40,50]
c = b.pop()
print("经过c = b.pop()后b的元素为：")
print(b)
print("经过c = b.pop()后c的元素为：")
print(c)
