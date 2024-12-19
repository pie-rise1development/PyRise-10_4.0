import phonenumbers
from phonenumbers import timezone, geocoder, carrier

print('')
print('Информация о номере телефона:')
print('-')
x = phonenumbers.parse('+79495616430')

valid = phonenumbers.is_valid_number(x)

possible = phonenumbers.is_possible_number(x)


Carrier = carrier.name_for_number(x, 'ru')

Region = geocoder.description_for_number(x, 'ru')

timeZone = timezone.time_zones_for_geographical_number(x)

print("Кодовая цифра номера телефона -", x)
print('Континент, где был зарегистрирован номер телефона:', '/'.join(timeZone))
print("Оператор связи:", Carrier)
print("Страна номера телефона:", Region)
print(f"Существование номера телефона ( В НАСТОЯЩЕМ ВРЕМЕНИ! ): {valid}, перевод значений ниже  - ↓ ↓ ↓")
print(f"Теоритическое существование номера телефона: {possible}, перевод с английского: [True: Да], [False: Нет].")
print(f'Номер телефона: +79495616430')
print('')