
user_name = 'Charlie'
user_age = 18

print ("读者名：" , user_name, "年龄:"  ,user_age, sep='|')

f = open("poem.txt","w")
print('沧海明月珠有泪',file=f)
print('大炮6666',file=f)

f.close()


print(40,'\t',end="")
print(50,'\t',end="")
print(60,'\t',end="")