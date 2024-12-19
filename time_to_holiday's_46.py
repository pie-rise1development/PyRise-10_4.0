from datetime import datetime, timedelta

def countdown_to_holiday(holiday_date):
    now = datetime.now()
    if holiday_date < now:
        return "Праздник уже прошёл!"

    delta = holiday_date - now
    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"До праздника который вы указали в консоли осталось: {days} дней, {hours} часов, {minutes} минут."

if __name__ == "__main__":
    # Установите дату праздника (например: Новый Год.)
    holiday = datetime(2025, 6, 3) #Новый Год 2024 года.
    print(countdown_to_holiday(holiday))

print("-")
print("")
print("-")
print("Небольшая заметка: вначале пишите год, потом месяц, день.")

