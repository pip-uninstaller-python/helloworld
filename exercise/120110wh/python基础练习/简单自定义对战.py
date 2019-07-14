##自定义人物对战
##A与B的血量由系统定义
##玩家操作A
##系统操作B
print("Author：PengFei Tian")
print("Time: 2019-07-14 12:30 ")
print("{0:=^50}".format("程序开始"))
player = input("请输入英文玩家姓名：")
print("{0:-^50}".format('-'))
print("{0:-^50}".format(player))
print("{0:-^50}".format('-'))
#初始化玩家血量及攻击力
player_life = 0
player_attack = 0
#机器小夫固定血量
boos_life = 10
boos_attack = 10
#欢迎玩家
print("欢迎玩家：{}".format(player))
print("{0:-^50}".format('-'))
#显示初始化血量
print("玩家{}的初始血量为'{}'，攻击力为'{}'".format(player,player_life,player_attack))
print("{0:-^50}".format('-'))
print("接下来与你对战的机器玩家是->小夫<-")
print("{0:-^50}".format('-'))
print("游戏现在开始！")
print("{0:-^50}".format('-'))
#选择
print("请选择你要进行的操作：")
print("{0:-^50}".format('-'))
print("1.练级")
print("2.对战")
print("3.逃跑")
print("{0:-^50}".format('-'))

#选择后
while True:
    choose = int(input("请输入数字[1-3]:"))
    #玩家选择练级
    if choose == 1:
        player_life += 2
        player_attack += 2
        print()
        print("恭喜你升级成功，血量增加到{}，攻击力增加到{}".format(player_life,player_attack))
        print("{0:-^50}".format('-'))
    #玩家选择对战
    elif choose == 2:
        print("{}对->机器小夫<-进行攻击，血量减少{}".format(player,player_attack))
        print("{0:-^50}".format('-'))
        boos_life -= player_attack
        print("机器小夫剩余血量{}".format(boos_life))
        print("{0:-^50}".format('-'))
        #判断小夫生死
        #已死的话跳出判断结束
        if boos_life <= 0:
            print("机器小夫已被击败，战斗胜利！")
            break
        #未死的话，机器小夫将进行反击
        else:
            player_life -= boos_attack
            print("->机器小夫<-对{}进行反击，血量减少{}".format(player, boos_attack))
            print("{0:-^50}".format('-'))
            #反击
            if player_life <= 0:
                print("很遗憾，你被机器小夫打败了！")
                break
            #如果反击没把玩家击败将返回上一级
            else:
                continue
    #玩家选择逃跑
    elif choose == 3:
        print("{0:-^50}".format('-'))
        print("你可真是一个胆小鬼！")
        break
    #输入错误提醒
    else:
        print("输出错误，请重新输入")
        continue
#结束！
print("{0:-^50}".format('-'))
print("程序结束！")