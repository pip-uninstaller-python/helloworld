import requests
import re
import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, db='db', user='root', password='root', charset='utf8')
cursor = db.cursor()

def getimageslist(page=1):
    html = requests.get("https://www.doutula.com/article/list/?page={}".format(page)).text
    reg = r'data-backup="(.*?)".*?alt="(.*?)"'
    reg = re.compile(reg, re.S)
    imageslist = re.findall(reg, html)
    for x in imageslist:
        image_url = x[0]
        image_title = x[1]
        cursor.execute("insert into images(`name`, `imageUrl`) values('{}','{}')".format(image_title, image_url))
        # print(image_url, image_title)
        print("正在保存 %s" % image_title)
        db.commit()


for i in range(1, 3):
    print('第{}页'.format(i))
    getimageslist(i)
