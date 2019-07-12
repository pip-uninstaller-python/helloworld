def chuli(str):
    a=','.join(item[str+'欧赔'][:3])+item[str+'f返还率'][0]
    b = ','.join(item[str + '欧赔'][3:]) + item[str + '返还率'][1]
    c=','.join(item[str+'让球欧赔'][:3])+item[str+'让球返还率'][0]
    d= ','.join(item[str + '让球欧赔'][3:]) + item[str + '让球返还率'][1]
    e=','.join(item[str+'即时大小'])
    f=','.join(item[str+'变化时间'])
    g=','.join(item[str+'初始大小'])
    final=f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}'