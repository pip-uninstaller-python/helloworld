dirs=[lambda x,y:(x+1,y),#定义四个方向
      lambda x,y:(x-1,y),
      lambda x,y:(x,y+1),
      lambda x,y:(x,y-1)]
def qiujie(x1,y1,x2,y2):#x1，y1起点 x2,y2终点
    res=[]#定义一个空列表存储走过的路劲，方便最终路径的输出
    res.append((x1, y1))
    while len(res)>0:
        now=res[-1]
        if now[0]==x2 and now[1]==y2:#到达终点输出路径
            for i in res:
                print(i)
            return 1
        for dir in dirs:#分别试探四个方向
            nex=dir(now[0],now[1])
            if map[nex[0]][nex[1]]==0:
                res.append(nex)
                map[nex[0]][nex[1]]=2
                break
        else:
            res.pop()
    else:
        print('无出路')
        return 0
map=[[1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,0,0,0,1,0,1],
     [1,0,0,1,0,1,0,0,0,1],
     [1,0,0,0,0,1,1,1,0,1],
     [1,1,1,1,1,1,1,1,1,1]]
qiujie(2,1,3,8)