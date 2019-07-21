import time
a=int(time.time())
print(a)
a=time.localtime(a)
print(a)
a=time.strftime('%Y-%m-%d %H:%M:%S',a)

print(a)
a=time.mktime()
print(a)
# 15636792083655
# 15636799444329
# 15636799551400
# 15636799246329.998
# 1563679882