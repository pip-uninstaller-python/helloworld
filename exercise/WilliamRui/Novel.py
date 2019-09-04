####################################################################################################################
'''
V01  20190820
---Initial Version
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
---修改函数结构，方便多线程调用
---修改因循环范围上限导致小说最后一章没有正常下载的BUG
---导入多线程下载，可加快约6倍左右的下载速度
---加入时间模块，用于记录程序运行时间
---新增输出信息，包含最新章节名称、下载结束提示及下载用时信息
V05  20190825
---修复因根据索引词无法找到小说而导致在选择小说界面无限死循环的BUG
---将小说part更改为从part1开始
V06  20190904
---导入PrettyTable模块，美化索引结果的输出
'''
####################################################################################################################
import requests
from bs4 import BeautifulSoup
import time
import threading
from prettytable import PrettyTable

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.100 Safari/537.36"}


# This part get the Soup of the response of a link
def getSoup(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup


# This part get the content of a chapter, which is what we need.
def getContent(url):
    Soup = getSoup(url)
    ChapterName = Soup.find('div', class_='bookname').find('h1').text
    Content = Soup.find('div', id='content').text
    Content = Content.replace('\u00a0\u00a0\u00a0\u00a0', '\n')
    Content = ChapterName + '\n\n' + Content + '\n'
    return Content


# This part get the links of the chapters in the catalogue page
def getChapterLink(url):
    Soup = getSoup(url)
    BookName = Soup.find('div', id='info').find('h1').text
    ChapterLinks = []
    Chapters = Soup.find('div', id='list').find('dl').findAll('dd')
    LatestChapter = Soup.find('div', id='info').findAll('p')[-1].find('a').text
    for Chapter in Chapters:
        ChapterLink = 'https://www.xbiquge6.com/' + Chapter.find('a').get('href')
        ChapterLinks.append(ChapterLink)
    return BookName, ChapterLinks,LatestChapter


# This part download the contents of the chapters we set(base on the region we give)
def partDownLoad(ChapterLinks, i, j, k):
    print('正在下载Part{}...\n'.format(k+1))
    global Contents
    ChapterContent = ''
    for ChapterLink in ChapterLinks[i:j]:
        ChapterContent = ChapterContent + "\n" + getContent(ChapterLink)
    Contents[k] = ChapterContent
    print('Part{}下载完成\n'.format(k+1))


# This part get the url of the book user needs.
def getBookLink():
    # 让用户输入小说名称，以一定格式返回搜索结果
    # 让用户根据显示的搜索结果选择小说对应的编号，然后函数反馈用户选择小说的地址
    SearchName = input('请输入搜索关键词：')
    while True:
        SearchUrl = 'https://www.xbiquge6.com/search.php?keyword=' + SearchName
        # 拼凑出搜索结果的地址
        Soup = getSoup(SearchUrl)
        Books = Soup.findAll('div', class_='result-item result-game-item')
        if Books:
            i = 1
            tb = PrettyTable(['序号', '书名', '作者', '链接'])
            for Book in Books:
                BookName = Book.find('a', cpos='title').get('title')
                BookLink = Book.find('a', cpos='title').get('href')
                Author = Book.find('p', class_='result-game-item-info-tag').findAll('span')[1].get_text().strip()
                i = i + 1
                tb.add_row([i, BookName, str(Author), BookLink])
            print(tb)
            BookID = int(input('请输入目标小说ID：'))
            while True:
                # 防止用户输入的书编号不正确，此处使用死循环加条件语句
                if 0 < BookID < len(Books) + 1:
                    # 防止用户输入的小说编号不符合要求
                    return Books[BookID - 1].find('a',cpos='title').get('href')
                else:
                    BookID = int(input('小说序号输入有误，请重新输入:'))
        else:
            SearchName = input('未找到相关小说，请重新输入搜索关键词：')


# Get the time when the program start.
t1 = time.time()
Pool = []
global Contents
Contents = []
url = getBookLink()
BookName, ChapterLinks,LatestChapter = getChapterLink(url)
# Put the calculations out of the loop to avoid extra calculations.
A = len(ChapterLinks)
B = int(A / 10)
for i in range(10):
    Contents.append('')
    # For the last part, the region is not the same as it in the other ones.
    # It may cause index out of range if we treat it like the others.
    if i == 9:
        T = threading.Thread(target=partDownLoad, args=(ChapterLinks, B * i, A, i))
    else:
        T = threading.Thread(target=partDownLoad, args=(ChapterLinks, B * i, B * (i + 1), i))
    T.start()
    # Store the threads in a list so that we can join them later, can't join the threads here,
    # or else the loop will be blocked, which means the threads will run in order, not parallel.
    Pool.append(T)
# Block the main thread
for T in Pool:
    T.join()
# Merge the contents we got, and save it in file.
with open(BookName + '.txt', 'a', encoding='utf-8')as T:
    for Content in Contents:
        T.write(Content)
# Get the time when the program ends.
t2 = time.time()
# Print the result and how long it takes to download the book.
print('{}已成功下载\n最新章节为:{}\n用时:{}\n'.format(BookName,LatestChapter, t2 - t1))
