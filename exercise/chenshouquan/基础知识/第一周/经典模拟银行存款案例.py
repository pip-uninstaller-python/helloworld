#模拟银行存款的项目
#1.模拟3张一行卡，1001,1002,1003，分别设置密码和余额（可以用9个变量分别保存卡号密码和余额）
#b.提示用户输入银行卡和密码
#c.如果用户输入正确—————提示让用户选择取款、存款还是退出并提示余额多少，输入错误重新输入卡号密码
#d.选择取款---提示输入取款额度。如果超过余额，提示余额不足，否则在余额上减掉相应金额
#e.选择存款---输入存款额度，余额加上相应额度并提示余额多少
#f.选择退出---重新输入卡号和密码
#g.设置 3次输入错误账号密码锁定被已卡银行提示
#h.特别注意换行后缩进全部用Tab字符间空格用空格
card1="1001"#变量卡号1
pwd1="123456"#变量密码1
ban1=10000#变量余额1

card2="1002"#变量卡号2
pwd2="123456"#变量密码2
ban2=10000#变量余额2

card3="1003"#变量卡号3
pwd3="123456"#变量密码3
ban3=10000#变量余额3
print("欢迎来到Python银行！")#提示语
times=0#赋值time表示次数
while True:#注意关键字首字母要大写自动循环

	card=input("请输入银行卡号！")
	pwd=input("请输入密码：")

	ban=0 #余额

	if card==card1 and pwd==pwd1:
		ban=ban1
	elif card==card2 and pwd==pwd2:
		ban=ban2
	elif card==card3 and pwd==pwd3:
		ban=ban3
	else:
		times=times+1
		if times>=3:
			print("你已经3次输入错误，联系银行柜台！")
			break#暂停全部循环
		else:
			print("卡号密码输入错误！请重新输入！")
			continue

	while True:
		num=input("请输入要办理的业务：1.存款 2.取款 3.退卡")
		if num=="1":
			inn=float(input("请输入存款金额："))#定义一个存款变量inn浮点型
			if inn<=0:
				print("存款金额请大于0！")
				continue
			else:
				ban=ban+inn
				print("存款成功！存入：",inn,"余额：",ban)
		elif num=="2":
			out=float(input("请输入取款金额："))
			if out>ban:
				print("余额不足赶紧去存钱！")
				continue
			else:
				ban=ban-out
				print("取款成功！取出：",out,"余额：",ban)
		elif num=="3":
			print("请收好卡片欢迎下次再来！")
			break
		else:
			print("输入有误！")
			continue

