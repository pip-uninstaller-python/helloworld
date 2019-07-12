# coding: utf-8
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
#my_friend = ensure_one(bot.search('春生'))
tuling = Tuling(api_key='340dad825e784010933c9e733ab53169')


# 使用图灵机器人自动与指定好友聊天
@bot.register()
def reply_my_friend(msg):	
    print(msg)
    tuling.do_reply(msg)




# 进入 Python 命令行、让程序保持运行
embed()