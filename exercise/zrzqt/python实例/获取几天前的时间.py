import time
import datetime
# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
#转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
#转换为其他字符串格式
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)
#第二种给定时间戳
'''
import time
import datetime
 
#给定时间戳
timeStamp = 1564931700
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray - datetime.timedelta(days = 3)
print(threeDayAgo)
'''
