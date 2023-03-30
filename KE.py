import pyautogui
import time


# time.sleep(2)
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)

pyautogui.click(715, 1057)


pyautogui.click(1650, 400)

time.sleep(3)
pyautogui.click(466, 349)

pyautogui.press('tab')
pyautogui.press('capslock')
pyautogui.press('enter')

pyautogui.press('tab')
pyautogui.press('capslock')
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab')
pyautogui.press('capslock')
for i in range(5):
    pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('tab')
pyautogui.press('capslock')
pyautogui.press('enter')

pyautogui.press('tab')
pyautogui.press('capslock')
pyautogui.press('enter')

pyautogui.scroll(-1000)

pyautogui.click(160, 129)
pyautogui.click(160, 620)
pyautogui.click(160, 670)
pyautogui.click(160, 720)

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(1)
pyautogui.scroll(-3000)
y = 181
for i in range(12):
    pyautogui.click(160, y)
    y+=55

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(1)
pyautogui.scroll(-3000)

pyautogui.click(161, 116)
pyautogui.click(161, 216)
time.sleep(4)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)