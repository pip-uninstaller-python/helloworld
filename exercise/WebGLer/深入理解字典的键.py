spam = {'show':'red',
        'describ': 'color',
        }
if 'color' not in spam:     #表明的是spam这个字典中是否含有‘color’这个键
    spam['color'] = 'blue'
    print(spam['color'])
else:
    print('别改了')