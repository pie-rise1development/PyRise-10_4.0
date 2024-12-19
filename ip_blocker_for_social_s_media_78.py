import requests
from colorama import Fore
import random

def deanon(ip: str):
    user_agent = random.choice(["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36"])
    req = requests.get(f"http://ip-api.com/json/{ip}?lang=ru", headers={"Accept-Language":"ru-RU", "User-Agent":user_agent})
    if req.status_code != 200:
        print(F"{Fore.RED} | Не удалось обработать запрос, попробуйте ещё раз...")
    else:
        data = req.json()
        if data['status'] == 'fail':
            print(f"{Fore.RED} | Данный IP не существует, или возникла неполадка с системой программы!")
        else:
            results = []
            for key, value in data.items():
                results.append(f"{key.title()}:{value}")
            return results
        
if __name__ == '__main__':
    data = deanon(input(f"Введите IP сервера, про который хотите узнать информацию: "))
    if data:
        print(data)