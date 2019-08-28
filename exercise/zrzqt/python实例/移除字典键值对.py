test_dict = {'zrzqt': 1,'baidu': 2,'google':3,'zhihu':4}
#输出原始字典
print('字典移除前：'+str(test_dict))
#使用del移除zhihu
del test_dict['zhihu']
#输出移除后的字典
print('字典移除后：'+str(test_dict))
#移除没有的key报错
#del test_dict['taobao']
