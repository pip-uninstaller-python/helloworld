#不定长参数
'''def addd(a,b,c,d):#这个是确定的参数长度
	summ=a+b+c+d #对其求和
	return summ 
print(addd(3,45,7,5))'''
def addd(*args):#用*+字母表示不定长参数（字母随便写）通常用args
	summ=0#赋值变量0
	for i in args:#遍历args里每个值
		summ=summ+i
	return summ
d=addd(2,23,10,10)
print(d)
	