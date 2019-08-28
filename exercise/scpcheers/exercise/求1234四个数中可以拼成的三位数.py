# 总共的
b = []
for  x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            b.append(int(f'{x}{y}{z}'))
print(f'总共有{len(b)}个数.\n分别是：')
print([i for i in b])

# 互不相同且没有相同数字
b = []
for  x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x!=y) and (x!=z) and (y!=z):
                print(x,y,z)
