import pyautogui
import time

# 获取鼠标当前位置
try:
    while True:
        positionStr = '>'
        for i in range(60):
            print(positionStr, end='')
            positionStr += '>'
            time.sleep(1)
            i+=1
            print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')
