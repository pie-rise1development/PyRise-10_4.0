import pyjokes

# Получаем случайную шутку
joke = pyjokes.get_joke(language='ru')
# Выводим полученную шутку
print(joke)