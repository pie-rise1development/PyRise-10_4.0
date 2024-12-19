import hashlib
import time

class SimpleCoin:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.balance = 0
        
    def main(self, amount):
        self.balance += amount
        question = input(f"Пожалуйста подождите пока банк подсчитает полную сумму выдачи купюр... [ Нажмите на клавишу 'Enter' для дальнейшей обработки ваших средств. ]")
        print(f"-")
        print(f"Подготавливается!")
        time.sleep(7.9)
        print(f"Осталось 3 минуты.")
        time.sleep(8.5)
        print(f"Готово! Теперь ваше финансовое состояние измеряется в: {self.balance} ({self.symbol})")
        
    def get_balance(self):
        return self.balance
    
# Пример использования.
coin = SimpleCoin("Pie-Coinage1", "*RC-1")
coin.main(1)
print("")
print(f"Теперь вы можете за счёт данной валюты купить, что-то в скоро-доступном магазине, также, ваш итоговый баланс отображается здесь: {coin.get_balance()} ({coin.symbol})")