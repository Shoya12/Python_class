"""
print('Whatsapp Automation Project')
import pyautogui as py # type: ignore[reportMissingModuleSource]
import time 
py.hotkey('command','space')
time.sleep(1)

py.write('Whatsapp')
time.sleep(1)
py.press('return')

time.sleep(3)
py.hotkey('command','f')

time.sleep(2)
py.write('Python Shrawan Class')

py.press('return')
time.sleep(2)

task='Write a small review about python class(automation try)'
py.write(task)
time.sleep(1)

py.press('return')
print('Whatsapp automation is complete ')

"""