import datetime
import requests

def get_sun_times(lat, lon):
    url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&formatted=0"
    response = requests.get(url)
    data = response.json()

    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    
    # Преобразование времени в читаемый формат
    sunrise = datetime.datetime.fromisoformat(sunrise).astimezone()
    sunset = datetime.datetime.fromisoformat(sunset).astimezone()
    
    return sunrise.strftime('%H:%M:%S'), sunset.strftime('%H:%M:%S')

if __name__ == "__main__":
    latitude = 55.7558  # Например, Москва
    longitude = 37.6173  
    
    sunrise_time, sunset_time = get_sun_times(latitude, longitude)
    print("Приветствую! Вы присоединились к осмотру восхода и заката солнца каждый день. Удачного использования.")
    print("-")
    print(f"1.) Время, во сколько восходит солнце: {sunrise_time} [ Утро ]")
    print("-")
    print(f"2.) Солнце погружается в ночь: {sunset_time} [ Вечер ]")
    print("")