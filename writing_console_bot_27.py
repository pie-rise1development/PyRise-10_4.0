gameloop = True
while gameloop:
    print('Вы:')
    rep = input().lower()
    if rep == 'привет':
        print('Здравствуйте!')
    elif rep == 'до свидания.':
        print('Пока, желаю вам хорошего продолжения дня!')
        gameloop = False
    else:
        print('Извините, но я вас не понимаю, попробуйте перезапустить меня...')