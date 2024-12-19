import speedtest

def speed_test():
    st = speedtest.Speedtest()

    print("Пожалуйста подождите, я ищу вашу сеть Wi-Fi!")
    st.get_best_server()

    print("Опа, кажись получилось. Пытаюсь потребить информацию...")
    download_speed = st.download() / 1_000_000 # Конвертация в Мбит/с
    print("Сейчас попробую опубликовать статистические данные.")
    upload_speed = st.upload() / 1_000_000     # Конвертиция в Мбит/с
    ping = st.results.ping

    print(f"Скорость загрузки интернет запросов: {download_speed:.2f} Мбит/с ✨")
    print(f"Скорость выгрузки: {upload_speed:.2f} Мбит/с 💝")
    print(f"Ваш Пинг: {ping} MC 🥰")

if __name__ == "__main__":
    speed_test()

with open(__file__) as f:
    print(f.read())
