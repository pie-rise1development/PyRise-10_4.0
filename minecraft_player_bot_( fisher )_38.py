from javascript import require, On

mineflayer = require('mineflayer')

bot = mineflayer.createBot({
    'host': 'pie_rie_100.aternos.me',
    'username': 'Risovick1Bot',
    'version': '1.12.2'
})


@On(bot, 'chat')
def msgHandler(this, user, message, *args):
    if user != 'Risovick1Bot':
        bot.chat(f'Приветствую, {user}! Я внебрачный сын Пирожка с Рисом, могу помочь с чем угодно так-как уроки их жопы.')

            