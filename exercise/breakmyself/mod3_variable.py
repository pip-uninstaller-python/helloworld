# -*- coding: utf-8 -*-
# 开发团队   ：pip uninstall python
# 开发人员   ：breakmyself
# 开发时间   ：2019/7/30  11:48 
# 文件名称   ：mod3_variable.PY
# 开发工具   ：PyCharm
#github主页：https://github.com/breakmyself
#变量   variable
#给 a  赋值 为5，打印a可以获取到a的值
a = 5
print(a)
print(type(a))
#输出结果<class 'int'>  类型是int
#将a再次赋值，a会有新的值传入这个时候a就不是5 而是 Hello，Charlie
a = ("Hello,Charlie")
print(a)
print(type(a))
#输出结果 <class 'str'> 类型是str

user_name = 'Charlie'
user_age = 8
print("读者姓名：",user_name,"年龄：",user_age)
#运行结果：读者姓名： Charlie 年龄： 8
#使用sep进行分割
user_name = 'Charlie'
user_age = 8
print("读者姓名：",user_name,"年龄：",user_age,sep='|')
#输出结果：  读者姓名：|Charlie|年龄：|8
#设置end参数，指定输出之后不再换行：
print(40,'\t',end="")
print(50,'\t',end="")
print(60,'\t',end="")
#输出结果：40 	50 	60
