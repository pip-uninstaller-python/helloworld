while True:
    number=input("请输入一个正数:(输入q退出程序）")
    if number in ['q','Q']:
        break
    elif not float(number)>0:
        print("请输入一个正数（输入q退出程序）：")
    else:
        number=float(number)
        array1=[]
        array2=[]
        integer=int(number)
        floa=number-integer
        while integer!=0:
            array1.append(integer%2)
            integer=integer//2
        else:
            array1.append(0)
        array1.reverse()
        while floa>0.00001:
            array2.append(int(2*floa))
            floa=floa*2-int(floa*2)
        else:
            array2.append(0)
        array1.append(".")
        array=array1+array2
        for x in array:
            print(x,end="")
        print("\n")
