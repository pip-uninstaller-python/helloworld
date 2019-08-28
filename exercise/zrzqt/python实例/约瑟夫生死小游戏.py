#30 个人在一条船上，超载，需要 15 人下船。
#于是人们排成一队，排队的位置即为他们的编号。
#报数，从 1 开始，数到 9 的人下船。
#如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船
people={}
for x in range(1,31):
    people[x]=1
# print(people)
check=0
i=1
j=0
while i<=31:
    if i== 31:
        i=1
    elif j== 15:
        break
    else:
        if people[i] == 0:
            i+=1
            continue
        else:
            check+=1
            if check == 9:
                people[i]=0
                check = 0
                print('{}号下船了'.format(i))
                j+=1
            else:
                i+=1
                continue
