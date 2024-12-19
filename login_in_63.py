from telethon import TelegramClient

# Ваши данные.
api_id = '27704018'
api_hash = 'b896b43a613c53b036a7d63ad46fe2d0'
phone_number = ''

# Создание клиента.
client = TelegramClient('randol_beacher_1', api_id, api_hash)

async def main():
    await client.start()

    # Например, отправка сообщения себе.
    me = await client.get_me()
    await client.send_message(me, 'Привет! Это тестовое сообщение.')

# Запуск клиента.
with client:
    client.loop.run_until_complete(main())