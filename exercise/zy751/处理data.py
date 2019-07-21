data='''
i: 苹果
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15636741871533
sign: 286d756d28b32ff123ff84c2e53f997e
ts: 1563674187153
bv: f0325f69e46de1422e85dedc4bd3c11f
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
'''
data=data.split('\n')
data=data[1:-1]
dict={}
for i in data:
    dict[i.split(':')[0]]=i.split(':')[1].strip()
print(dict)