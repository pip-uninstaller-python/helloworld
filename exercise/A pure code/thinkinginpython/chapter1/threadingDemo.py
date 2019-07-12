import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features='lxml')
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("Could not find comic image")
        else:
            comicUrl = comicElem[0].get('src')
            print('Downloading image http:%s...' % (comicUrl))
            res = requests.get('http:' + comicUrl)
            res.raise_for_status()
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(1000000):
                imageFile.write(chunk)
            imageFile.close()


downloadTreads = []
for i in range(1, 21, 5):
    downloadTread = threading.Thread(target=downloadXkcd, args=[i, i + 5])
    downloadTreads.append(downloadTread)
    downloadTread.start()

# 当我们调用某个线程的这个方法时，这个方法会挂起调用线程，直到被调用线程结束执行，调用线程才会继续执行。
for t in downloadTreads:
    t.join()
print('\nDone')
