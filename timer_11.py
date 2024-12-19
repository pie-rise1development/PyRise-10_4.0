import time

while True:
    i = 0 # секунды
    ii = 0 # минуты
    iii = 0 # часы
    time_user = int(input(" Введите количество секунд: "))
    comment = str(input("Введите ваш комментарий: "))
    for q in range(time_user):
        time.sleep(1)
        i += 1
        print(" Истекло секунд: ", i)
        if( i % 60) == 0:
            ii += 1
            print("Истёкло минут: ", ii)
        if(i % 3600) == 0:
            iii += 1
            print("Истекло часов: ", iii)

print("Ваше время истекло!")
print(" Ваш комментарий:", comment)

