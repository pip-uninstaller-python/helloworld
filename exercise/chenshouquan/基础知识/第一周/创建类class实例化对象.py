class Dog(object):
	typee="宠物"#类变量
	#初始化方法
	def __init__(self,name, age,color):#def __init__初始化方法

		self.name=name #实例变量（属性）
		self.age=age #实例变量（属性）
		self.color=color #实例变量（属性）

	def eat(self):#普通方法
		print(self.name,"狗狗在啃骨头！")

	def run(self,speed):#普通方法
		print(self.name,"狗狗在飞快的跑！速度",speed)
		
#实例化对象
dog=Dog("小黑",3,"白色")#用小写dog去接收
dog.color="黑色"#可以对属性修改
print(dog.name)#对象属性显示
dog.eat()#调用方法
dog.run("3m/s")