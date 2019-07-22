#json
#简单来讲，json就是js中的对象
#{key:value,key:value......}json和字典类似
#本质上讲,json就是有特定结构的字符串

import json

#json转字典
j='{"city":"北京","name":"熊猫"}'
p=json.loads(j)
print(type(p))
print(p) #{'city': '北京', 'name': '熊猫'}


#字典转json
dictt={"city":"北京","name":"熊猫"}
ss=json.dumps(dictt,ensure_ascii=False)
print(type(ss))
print(ss)#{"city": "北京", "name": "熊猫"}

