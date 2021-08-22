import pyautogui
import time
import keyboard


def detect_image(path, duration=0):
    while keyboard.is_pressed('u') == False:
        image_location = pyautogui.locateCenterOnScreen(path, confidence=0.99)
        if image_location:
            pyautogui.click(
                image_location[0], image_location[1], button='right', duration=duration)
            time.sleep(0.1)
            pyautogui.click(
                image_location[0], image_location[1]+50, duration=duration)
            print(path+" deleted")
            return True
        else:
            return False


while keyboard.is_pressed('u') == False:
    if detect_image("ajatite.png") == False and detect_image("valkite.png") == False:
        pyautogui.moveTo(1000, 500)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        time.sleep(0.5)
