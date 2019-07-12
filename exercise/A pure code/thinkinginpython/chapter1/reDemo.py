import re

print("使用括号()对查找结果分组")
p = re.compile(r'(\(\d\d\d\d\))-(\d\d-\d\d\d)')
q = p.search('hfdkf-(0111)-22-333-4444@qq.com-44-5555-9ff')
m, n = q.groups()
print(m, n)

print("使用管道符|匹配多个分组")

print("单纯管道")
p = re.compile(r'hello|world')
q = p.search('hello-world')
print(q.group())
q = p.search('world-hello')
print(q.group())
q = p.findall('hello-world')
print(q)

print("管道加上分组")
p = re.compile(r'tom(cat|dog|cow)')
q = p.search('my name is tomdog')
print(q.group())

print("用问号？匹配零次或一次")
p = re.compile(r'tom(one)?cat')
q = p.search("my name is tomcat")
print(q.group())
q = p.search("my name is tomonecat")
print(q.group())

print("用星号*匹配零次或多次")
p = re.compile(r'tom(one)*cat')
q = p.search("my name is tomcat")
print(q.group())
q = p.search("my name is tomonecat")
print(q.group())
q = p.search("my name is tomoneoneonecat")
print(q.group())

print("用加号+匹配一次或多次")
p = re.compile(r'tom(one)+cat')
q = p.search("my name is tomcat")
print(q)
q = p.search("my name is tomonecat")
print(q.group())
q = p.search("my name is tomoneoneonecat")
print(q.group())

print("用花括号{}匹配特定次数 {m,n} m,n为上下限")
p = re.compile(r'tom(one){1,3}cat')
q = p.search("my name is tomcat")
print(q)
q = p.search("my name is tomonecat")
print(q.group())
q = p.search("my name is tomoneoneonecat")
print(q)

print("用方括号[]单个匹配，匹配范围")
p = re.compile(r'[1-4]')
q = p.findall('123.45')
print(q)

print("贪心算法/非贪心算法")
print("问号在正则表达式中可能有两种含义：声明非贪心匹配或表示可选的分组。")
p = re.compile(r'(one){1,3}')
q = p.search("my name is oneoneoneone")
print(q.group())
p = re.compile(r'(one){1,3}?')
q = p.search("my name is oneoneoneone")
print(q.group())


# 长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字
def detection(text):
    if len(text) < 8:
        return False
    number = re.compile(r'(\d)+')
    print(number.search(text))
    if number.search(text) == None:
        return False
    number = re.compile(r'[A-Z]+')
    if number.search(text) == None:
        return False
    number = re.compile(r'[a-z]+')
    if number.search(text) == None:
        return False
    return True


print(detection("11CZA111"))
