#定义一个植物类
class Plant:
    role = 'plant'                        #植物的属性都是植物
#构造方法初始化
    def __init__(self, name, breed, att, life):
        self.name = name                #每个植物都有自己的昵称
        self.breed = breed              #每个植物都有自己的种类
        self.att = att    #每个植物都有自己的攻击力
        self.life = life        #每个植物都有自己的生命值
#定义植物攻击僵尸的方法
    def attack(self,corpse):
        corpse.life -= self.att #僵尸的生命值会根据植物的攻击力减少
#定义增长生命值的方法
    def eat(self):
        self.life += 50
#定义判断是否死亡的方法
    def die(self):
        if self.life <= 0:            #如果生命值小于等于0表示已被对方杀死
            print(self.name,'已死亡！')
        else:
            print(self.name,'的生命值还有',self.life)
#定义一个僵尸类
class Corpse:  
    role = 'corpse'                        #僵尸的属性都是僵尸
#构造方法初始化
    def __init__(self, name, breed, att, life):
        self.name = name                #每一只僵尸都有自己的昵称
        self.breed = breed              #每一只僵尸都有自己的种类
        self.att = att    #每一只僵尸都有自己的攻击力
        self.life = life        #每一只僵尸都有自己的生命值
#定义僵尸攻击植物的方法
    def bite(self,plant):
        plant.life -= self.att #植物的生命值会根据僵尸的攻击力而下降
#定义增长生命值的方法
    def eat(self):
        self.life += 30
#定义判断是否死亡的方法
    def die(self):
        if self.life <= 0:            #如果生命值小于等于0表示已被对方杀死
            print(self.name,'已死亡！')
        else:
            print(self.name,'的生命值还有',self.life)
#创建实例
plant1 = Plant('flower','花儿',30,1000)       #创造一个植物
corpse1 = Corpse('zoom','小僵尸',50,800)       #创造一个僵尸
plant1.die()                         #输出植物的当前状态
corpse1.die()                         #输出僵尸的当前状态
print('------开始-----')
plant1.attack(corpse1)                     #植物攻击僵尸一次
corpse1.bite(plant1)                       #僵尸攻击植物一次
plant1.die()                         #输出植物的当前状态
corpse1.die()                         #输出僵尸的当前状态
for i in range(20):                     #循环实现，植物攻击僵尸20次
    plant1.attack(corpse1)
corpse1.die()                         #输出僵尸的当前状态
plant1.eat()                         #植物吃一个阳光
plant1.die()                         #输出植物的当前状态

