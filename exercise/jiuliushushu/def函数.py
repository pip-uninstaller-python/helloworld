
def  menu(appetizer,course):
    print('一份开胃菜：'+appetizer)
    print('一份主食：'+course+'\n')
#还记得转义字符\n吧，表示换行
menu('牛肉拉面','话梅花生')
menu('话梅花生','牛肉拉面')
#如果采用下面这种形式传递，就不需要理会参数位置
menu(course='牛肉拉面',appetizer='话梅花生')

def pika2(name, person):
     print('我最喜爱的神奇宝贝是' + name)
     print('我最喜爱的驯兽师是' + person)
# 需要给两个参数分别赋值，并用逗号隔开，否则会报错
pika2('卡比兽', '小智')


def tree(Height):
    print('Merry Christmas!')
    for i in range(Height):
        print((Height-i)*2*'1'+'o'+ i*'~x~o')
        print(((Height-i)*2-1)*'1'+(i*2+1)*'/'+'|'+(i*2+1)*'\\')
tree(4)


for i in range(1,10):
    for j in range(1,i+2):
        print('%d X %d = %d' % (j,i,j*i) ,end = '  ')
    print('')