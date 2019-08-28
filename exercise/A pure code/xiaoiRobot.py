# coding: utf-8
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆

bot = Bot()
my_friend = ensure_one(bot.search('方研'))
xiaoi = XiaoI('open_1xLhpv7wDthj', 'U7si7Sdxw9X8EEovqnlY')

# 使用小 i 机器人自动与指定好友聊天
@bot.register()
def reply_my_friend(msg):
    xiaoi.do_reply(msg)


# 进入 Python 命令行、让程序保持运行
embed()


