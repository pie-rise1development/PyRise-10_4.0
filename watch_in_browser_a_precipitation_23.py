from urllib import response
from bs4 import BeautifulSoup
import requests


def weather_check(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36'
    }

    res = requests.get(f'https://www.google.com/search?q=погода+в+{city}', headers=headers)
    print(response)

    soup = BeautifulSoup(res.text, 'html.parser')

    time = soup.select("#wob_dts")[0].getText()
    precipitation = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    vether = soup.select('#wob_ws')[0].getText().strip()
    humidity = soup.select("#wob_hm")[0].getText()

    print('Город:',city)
    print("Время, а также день недели:",time)
    print('Окончательный результат осадков:',precipitation)
    print('Температура указанного города ( уличная температура ):',weather, '°C')
    print('Скорость ветра:',vether)
    print("Влажность на улице:",humidity)
    
    print("")
    print("-")
    print("")

    print("Developed by: Pie-Rise The Sound")
    print("")
    print("-")
    print("")
    print("Внимание:")
    print("Время вашего города может не совпадать с тем, что написано в таб-листе, так-как сервер, что используется в программе немного сломан...")
    print("Извините, если вдруг доставил неудобства.")

    

if __name__ == '__main__':
    city_input = input('Введите название города, о котором хотите узнать информацию: ')
    weather_check(f'{city_input}')