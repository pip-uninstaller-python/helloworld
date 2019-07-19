#列表排序
#列表升序
a = [20,10,50,30,80,40,90,55]
print("a = [20,10,50,30,80,40,90,55]")
print("id(a))=:")
print(id(a))
print("a.sort()=")
a.sort()
print(a)
print("a.sort()后id(a))=:")
print(id(a))


#列表降序
a.sort(reverse = True)

print("a.sort(reverse = True)=:")
print(a)
print(id(a))

