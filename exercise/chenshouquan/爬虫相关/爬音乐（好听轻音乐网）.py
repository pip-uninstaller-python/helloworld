#准备工作先安装requests模块
#使用pip工具下载安装CMD.exe输入pip install requests
#在D盘建立一个文件夹music
#第一个循环可以修改rangge（0,2）这样就可以不用重复下载
#
import re
import requests
import time

# #第一页网址
# http://www.htqyy.com/top/hot
# http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
# #第二页网址
# http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# #第三页
# http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
# #第四页
# http://www.htqyy.com/top/musicList/hot?pageIndex=3&pageSize=20
while True:
	page=int(input("请输入你要爬取的页数："))
	songID=[]
	songName=[]

	for i in range(0,page):
		url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"#地址构造
		#print(url)#检验地址

		#获取音乐榜单的网页信息
		html=requests.get(url)

		#print(html)#检验获取结果

		strr=html.text

		pat1=r'title="(.*?)" sid'#获取歌名 注意后面把空格+sid
		pat2=r'sid="(.*?)"'#获取序号



		idlist=re.findall(pat2,strr)
		titlelist=re.findall(pat1,strr)

		songID.extend(idlist)
		songName.extend(titlelist)

	#print(len(songID)) #检测ID和名字一样多就对了
	#print(songName) #检测ID和名字一样多就对了

	for i in range(0,len(songID)):

		#http://f2.htqyy.com/play7/34/mp3/7
		#http://f2.htqyy.com/play7/261/mp3/7

		songurl="http://f2.htqyy.com/play7"+str(songID[i])+"/mp3/7"#这个地址注意更新
		songname=songName[i]

		data=requests.get(songurl).content#requests字母要写全 歌曲是字节码要用content


		print("正在下载第",i+1,"首")

		with open("D:\\music\\{}.mp3".format(songname),"wb") as f:#写进D盘music文件夹 format代表当前村的是songname
			f.write(data)		


		time.sleep(0.5)


#歌曲url  http://www.htqyy.com/play/33

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
# wd={"wd":"中国"}
# response=requests.get("http://www.baidu.com/s?",params=wd,headers=headers)#请求
# data=response.text#返回一个字符串形式的数据
# data2=response.content#返回一个二进制形式的数据

# print(data2.decode())
