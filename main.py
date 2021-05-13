import keyboard
import pyautogui


def print_pressed_keys(e):
     # если клавиша нажата и имя клавиши 1
     if e.event_type == "down" and e.name == "1":
        print("<div>")
        #удаляем набранную 1
        pyautogui.press('backspace')
        #переводим курсор в самое начало
        pyautogui.press('home')
        #пишем <div>
        pyautogui.typewrite('<div>')

        
        
     elif e.event_type == "down" and e.name == "2":
        print("</div>")
        pyautogui.press('backspace')
        pyautogui.press('end')
        pyautogui.typewrite('</div>')
    #print(e, e.event_type, e.name)


keyboard.hook(print_pressed_keys)
keyboard.wait()
