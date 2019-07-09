# coding: utf-8
import socket
import requests, random, time, http
import pytesseract
from PIL import Image

def get_content_img():
    url = 'http://211.166.76.62/2019cjfb/register/image.jsp'
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            req = requests.get(url, headers=header, timeout=timeout)
            img = req.content
            with open('./a.png', 'wb') as f:
                f.write(img)
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))
        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))

if __name__ == "__main__":
    get_content_img()
    im = Image.open(r'D:\PycharmProjects\untitled1\a.png')
    print(im)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    num=pytesseract.image_to_data(im)
    print(num)
    print(num[-4:])
