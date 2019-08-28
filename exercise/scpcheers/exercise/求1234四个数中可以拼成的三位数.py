b = []
for  x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            b.append(int(f'{x}{y}{z}'))
print(f'总共有{len(b)}个数.\n分别是：')
print([i for i in b])
