#引入 datatime 模块
import datetime
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday
#输出
print(getYesterday())

#通过导入 datetime 模块来获取昨天的日期
