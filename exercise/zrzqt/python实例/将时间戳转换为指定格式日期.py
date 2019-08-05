import time
#获得当前时间戳
now = int(time.time())
#转换为其他日期格式
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
#第二种
'''
import datetime 
# 获得当前时间
now = datetime.datetime.now()
# 转换为指定的格式
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)
'''
#指定时间戳
'''
import time
timeStamp = 1564931700
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
'''
#第二种
'''
import datetime
timeStamp = 1564931700
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)
'''
