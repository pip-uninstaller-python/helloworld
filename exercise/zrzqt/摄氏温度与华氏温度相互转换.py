a = int(input('摄氏温度转换为华氏温度请按1\n华氏温度转换为摄氏温度请按2\n'))
while a != 1 and a != 2:
    a = int (input('你选择不正确，请重新输入。\n摄氏温度转换为华氏温度请按1\n华氏温度转换为摄氏温度请按2\n'))
if a == 1:
    celsius = float(input('输入摄氏温度：'))
    fahrenheit = (celsius * 1.8)+32#计算华氏温度
    print('%.1f摄氏温度转换为华氏温度%.1f'%(celsius,fahrenheit))
else:
    fahrenheit = float(input('输入华氏温度'))
    celsius = (fahrenheit - 32)/1.8#计算摄氏温度
    print('%.1f华氏温度转换为摄氏温度为%.1f'%(fahrenheit,celsius))
