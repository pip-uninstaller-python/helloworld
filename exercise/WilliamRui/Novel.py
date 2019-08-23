####################################################################################################################
'''
V01  20190820
---Initial Version
---基于之前版本重新写
V02  20190820
---在用户输入目标小说ID的时候，加入循环，并在循环中加入判断语句，防止用户输入的ID格式不正确，
   如用户输入不正确则重新要求用户输入字符
---在下载小说前后打印正在下载和下载完成字样
V03  20190821
---由于偶尔要引用此程序的部分函数，将获取小说名称部分移到GetChapterLinks函数中，方便后续引用
---将函数主体整合成一个main函数
---优化函数，将函数功能独立开，将相关变量挪到定义的函数外部获取
---使下载小说函数独立，只要给定link即可下载小说，方便后续调试
V04  20190823
---将获取章节链接独立出来
---利用多线程threading，加快程序运行速度
---增加时间部分，用于统计程序运行时间
'''
####################################################################################################################
from bs4 import BeautifulSoup
import requests，time，threading

def GetSoup(url):
    # 因程序中多出用到BeautifulSoup，为避免重复使用，此处直接定义函数获取Soup
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
    Resp = requests.get(url, headers=headers)
    Resp.encoding = Resp.apparent_encoding
    # 定义get到的网页信息的编码方式为网页html中的编码方式
    Soup = BeautifulSoup(Resp.text, "lxml")
    return Soup

def GetBookLink():
    # 让用户输入小说名称，以一定格式返回搜索结果
    # 让用户根据显示的搜索结果选择小说对应的编号，然后函数反馈用户选择小说的地址
    SearchName = input('请输入搜索关键词：')
    SearchUrl = 'https://www.xbiquge6.com/search.php?keyword=' + SearchName
    # 拼凑出搜索结果的地址
    Soup = GetSoup(SearchUrl)
    Books = Soup.findAll('div', class_='result-item result-game-item')
    print('{1:{0}<3}\t{2:{0}<8}\t{3:{0}<8}\t{4}'.format(chr(12288), '序号', '书名', '作者', '链接'))
    i = 1
    for Book in Books:
        BookName = Book.find('a', cpos='title').get('title')
        BookLink = Book.find('a', cpos='title').get('href')
        Author = Book.find('p', class_='result-game-item-info-tag').findAll('span')[1].get_text().strip()
        print('{1:{0}<3}\t{2:{0}<8}\t{3:{0}<8}\t{4}'.format(chr(12288), i, BookName, str(Author), BookLink))
        i = i + 1
    BookID = int(input('请输入目标小说ID：'))
    while True:
        # 防止用户输入的书编号不正确，此处使用死循环加条件语句
        if BookID > 0 and BookID < len(Books) + 1:
            # 防止用户输入的小说编号不符合要求
            return Books[BookID - 1].find('a',cpos='title').get('href')
        else:
            BookID = int(input('小说序号输入有误，请重新输入:'))

def GetContent(url):
    # 获取小说章节正文
    Soup = GetSoup(url)
    ChapterName = Soup.find('div', class_='bookname').find('h1').get_text()
    # 获取的正文没有段落换行，但是首行缩进识别了，这里我们将首行缩进替换为换行加四个空格，变相实现段落换行
    Content = Soup.find('div', id='content').get_text().replace('\u00A0\u00A0\u00A0\u00A0', '\n    ')
    Content = ChapterName + '\n' + Content
    # 将取到的章节名和正文结合作为一章
    return Content
def GetChapterLinks(url):
    # 获取小说的章节链接
    ChapterLinks = []
    Soup = GetSoup(url)
    BookName = Soup.find('div', id='info').find('h1').text
    DDs = Soup.find('div', id='list').find('dl').findAll('dd')
    for DD in DDs:
        ChapterLinks.append('https://www.xbiquge6.com' + DD.find('a').get('href'))
    return ChapterLinks, BookName

def DownLoad(i,j,k):
    print('第{}部分下载中...'.format(k))
    golbal Contents
    Contents[k]=''
    for Link in ChapterLinks[i,j]:
        Contents[k] = Contents[k] + GetContent(Link) 
    print('第{}部分下载完成'.format(k))
T1 = time.time()
BookLink = GetBookLink()
ChapterLinks, BookName = GetChapterLinks(BookLink)
Contents = []
B = len(ChapterLinks)
A = int(B/15)
Pool = []
for j in range(15):
    Contents.append('')
    if j != 14:
        T = threading.Thread(target=DownLoad,args=(A*i,A*(i+1),j))
    else:
        T = threading.Thread(target=DownLoad,args=(A*i,B,j))
    Pool.append(T)
    T.start()
for T in Pool():
    T.join()
with open(BookName+'.txt','a',encoding='utf-8')as T:
    for Content in Contents:
        T.write(Content)
print('{}下载完成'.format(BookName))
T2 = time.time()
print('下载{}用时{}'.format(BookName,T2-T1))

