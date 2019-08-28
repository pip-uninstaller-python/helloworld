#使用update()方法，第二个参数合并第一个参数
def Merge(dict1,dict2):
    return(dict2.update(dict1))
#两个字典
dict1 = {'a':10,'b':8}
dict2 = {'d':6,'c':4}
#返回 None
print(Merge(dict1,dict2))
#dict2合并了dict1
print(dict2)
#使用**，函数将参数以字典的形式导入
'''
def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
      
# 两个字典
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 
dict3 = Merge(dict1, dict2) 
print(dict3)
'''
