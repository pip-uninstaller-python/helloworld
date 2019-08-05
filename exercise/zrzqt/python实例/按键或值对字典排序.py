#按键(key)排序
def dictionairy():
    #声明字典
    key_value={}
    #初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print('按键(key)排序：')
    #sorted(key_value)返回一个迭代器
    #字典按键排序
    for i in sorted (key_value):
        print((i,key_value[i]),end='')
def main():
    #调用函数
    dictionairy()
#主函数
if __name__=='__main__':
    main()
#按值(value)排序
'''
def dictionairy():  
    # 声明字典
    key_value ={}     
    # 初始化
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 
    print ("按值(value)排序:")   
    print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))     
def main(): 
    dictionairy()               
if __name__=="__main__":       
    main()
'''
#字典列表排序
'''
lis = [{ "name" : "Taobao", "age" : 100},  
{ "name" : "zrzqt", "age" : 7 }, 
{ "name" : "Google", "age" : 100 }, 
{ "name" : "Wifi" , "age" : 200 }] 
  
# 通过 age 升序排序
print ("列表通过 age 升序排序: ")
print (sorted(lis, key = lambda i: i['age']) )
  
print ("\r") 
  
# 先按 age 排序，再按 name 排序
print ("列表通过 age 和 name 排序: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])) )
  
print ("\r") 
  
# 按 age 降序排序
print ("列表通过 age 降序排序: ")
print (sorted(lis, key = lambda i: i['age'],reverse=True) )
'''
