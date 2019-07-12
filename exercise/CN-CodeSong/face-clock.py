#打卡程序，拍照后自动与图库中的人员照片进行依次对比，获取最高相似度的人打卡成功

import requests          #pip install requests
import json
import base64
import os
import cv2              #pip install opencv-python
import time
import easygui          #pip install easygui


url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lVfov6E1oaWZR9f4qIhd9Hjy&client_secret=Gubrc6RnMTdA3Eb8WumHIGrz4vHgCTdy"

jue_path = os.getcwd()
try:
    os.mkdir("人脸识别打卡图库")        #创建文件夹，如果已经有了，就不做任何操作
except FileExistsError:
    pass

#UI界面
def ui():
    return easygui.buttonbox(msg="请选择需要的操作",choices=('新增人员','打卡','退出'))




#新增人员
def new_jober():
    xuan1 = ""
    name = ""
    os.chdir("人脸识别打卡图库/")
    while name == "":
        name = easygui.enterbox(msg = "请输入您的姓名")
    while xuan1 == "":
        xuan1 = easygui.msgbox(msg = "请拍摄照片（用于人脸识别打卡）" , ok_button = '拍摄照片(按"q"键拍照)')
    cap = cv2.VideoCapture(0)       #创建相机对象
    while(1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):       #按"q"键拍照退出
            cv2.imwrite("1.jpg", frame)         #保存照片
            break
    cap.release()
    cv2.destroyAllWindows()
    os.system("ren 1.jpg "+ name + ".jpg")          #更改图片名称
    os.chdir(jue_path)



#打开相机，进行拍照保存
def photo():
    cap = cv2.VideoCapture(0)       #创建相机对象
    while(1):
        
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):       #按"q"键拍照退出
            cv2.imwrite("2.jpg", frame)         #保存照片
            break
    cap.release()
    cv2.destroyAllWindows()




#1.获取AK的值，用于拼接接口

def get_url():
    html = requests.get(url)        #get请求url，获取所有数据
    text = html.text                #解析数据为文本
    text = eval(text[:-1])
    return text["access_token"]     #返回数据中的AK参数的数值



#2.读取图片，转换为base64编码 ——》接口需要

def imgdata(file1path, file2path):
    with open(file1path, "rb") as f:            #以二进制读取图片文件
        pic1 = base64.b64encode(f.read())       #更改图片文件的编码方式为“base64”

    with open('人脸识别打卡图库/' + file2path, "rb") as f:
        pic2 = base64.b64encode(f.read())

    params = json.dumps([
            {"image": str(pic1, "utf-8"), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},           #设置post请求的参数
            {"image": str(pic2, "utf-8"), "image_type": "BASE64", "face_type": "IDCARD", "quality_control": "LOW"},
        ])
    return params.encode()



#3.进行对比获取结果

def img(file1path, file2path):
    print("正在调用人脸识别...!")
    token = get_url()                               #调用get_url参数
    print("正在解析人脸图片...!")
    params = imgdata(file1path, file2path)          #调用读取图片参数（携带两张图片的路径）
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match" + "?access_token=" + token          #根据get_url函数返回的AK参数的数值，拼接url
    conten = requests.post(request_url, data=params).text           #post请求url（携带data参数），解析返回的数据为文本
    

    conten = json.loads(conten)             #利用"json"模块中的"loads"方法，将字符串转化为字典（用于后面判断）
    
    
    #print(conten)
    #print(type(conten))
    #print(conten[14])
    
    
    if conten['error_code'] == 0:           #如果用户上传的图片中人物差距过大，则post请求时会返回错误，“conten[error_code] == 0"用于检测是否有错误。
        conten = str(conten)
        content = eval(conten)
        score = content['result']["score"]              #从返回的文本中提取”相似度“

        p,l = os.path.splitext(file2path)
        p,name = os.path.split(p)
        a.append([score,name])



while True:
    a = []
    xuan0 = ui()
    if xuan0 == "打卡":
        photo()
        photo1 = '2.jpg'
        for photo2 in os.listdir("人脸识别打卡图库/"):             #依次调用图库中的照片
            img(photo1,photo2)
        try:
            if max(a)[0] < 60:
                print("未识别你是谁")
            else:
                print(max(a)[1]+"打卡成功")
        except ValueError:
            print("未识别你是谁")

        os.system("del 2.jpg")
    elif xuan0 == "新增人员":
        new_jober()
    elif xuan0 == '退出':
        break

    time.sleep(3)
