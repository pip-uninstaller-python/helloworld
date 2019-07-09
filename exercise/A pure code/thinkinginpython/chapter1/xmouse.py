import pyautogui
import time

'''
#获取鼠标当前位置
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        print(positionStr, end='')
        time.sleep(1)
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')
'''
time.sleep(4)
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, 0.2)
    distance -= 10
    pyautogui.dragRel(0, distance, 0.2)
    pyautogui.dragRel(-distance, 0, 0.2)
    distance -= 15
    pyautogui.dragRel(0, -distance, 0.2)
