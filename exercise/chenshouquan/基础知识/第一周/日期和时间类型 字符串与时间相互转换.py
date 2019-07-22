#日期和时间类型、时间与字符串相互转换
import datetime #引入时间包

#获取当前日期
now=datetime.datetime.now()
print(now) #2019-07-22 09:10:40.742608

#获取指定日期
d=datetime.datetime(2019,10,1,12,23,40)
print(d) #2019-10-01 12:23:40

#日期转字符串
now=datetime.datetime.now()
e=now.strftime("%Y-%m-%d %H:%M:%S")#%Y年 %m月 %d日 %H时 %M分 %S秒 注意月日小写
print(e) #2019-07-22 09:10:40

#字符串转日期
s="2020-8-15 2:30:20"
f=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
print(type(f))#打印下类型显示<class 'datetime.datetime'>
print(f) #结果2020-08-15 02:30:20