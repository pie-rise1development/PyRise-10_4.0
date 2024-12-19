import requests
from bs4 import BeautifulSoup

# URL для получения бесплатных прокси.
url = "https://sslproxies.org"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# Запрос на получение страницы с прокси.
response = requests.get(url, headers=headers)

# Парсим HTML-код с помощью BeautifulSoup.
soup = BeautifulSoup(response.content, "html.parser")
proxies = []

# Находим все строки с прокси.
for row in soup.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) >= 2: # Проверяем, что в строке есть минимум 2 столбца (IP и PORT)
        ip = columns[0].text.strip()
        port = columns[1].text.strip()
        proxies.append(f"{ip}:{port}")

# Выводим прокси в столбик.
print("Все рандомные прокси:")
print("")
for proxy in proxies:
    print(proxy)
print("")
print("DOWN LIST: ")
print("")
print("Прокси, что работают на 100%: ")
print("- 1. } \n- 2. } \n- 3. }\n")