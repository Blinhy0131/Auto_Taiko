import pyautogui

while(1):
    if(pyautogui.pixelMatchesColor(750,580,(243,71,40))==True):
        pyautogui.press('f')
    elif(pyautogui.pixelMatchesColor(750,580,(101,189,187))==True):
        pyautogui.press('d')
