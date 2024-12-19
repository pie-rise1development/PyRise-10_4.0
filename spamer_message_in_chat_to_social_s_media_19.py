import pyautogui
import time

print("Запуск был выполнен!")

def SendMessage():
    message = input("Введите сообщение:")
    amount  = 80000
    time.sleep(5)


    for i in range(amount):
        pass
    while amount > 0: 
        amount -= 1

        pyautogui.typewrite(message.strip())
        pyautogui.press("enter")

SendMessage()
                        