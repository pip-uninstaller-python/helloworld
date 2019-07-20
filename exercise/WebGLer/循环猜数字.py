import random
secret_number = random.randint(1,20)
print('这里有一个1-20之间的数字')
for guess in range(1,7):
    print('猜猜看数字是多少：')
    your_number = int(input())
    if your_number < secret_number:
        print('你猜的数字太小了，需要大一点')
    elif your_number > secret_number:
        print('你猜的数字太大了，需要小一点')
    else:
        break
if your_number ==secret_number:
    print('恭喜你，你在第'+str(guess)+'次猜对了我的数字')
else:
    print('哎，这个神秘的数字就是',secret_number)