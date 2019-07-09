# coding: utf-8
import time, datetime


def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]


now_week = get_week_day(datetime.datetime.now())
if now_week == "星期一":
    print("星期一")
elif now_week == "星期二":
    print("星期二")
elif now_week == "星期三":
    print("星期三")
elif now_week == "星期四":
    print("星期四")
elif now_week == "星期五":
    print("星期五")
elif now_week == "星期六":
    print("星期六")
elif now_week == "星期天":
    print("星期天")
