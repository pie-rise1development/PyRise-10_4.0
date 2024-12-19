from telegraph import Telegraph

# Создаём объект класса Telegraph
telegraph = Telegraph()
# Создаём аккаунт с именем 'test'
telegraph.create_account(short_name='test')

# Создаём страницу с заголовком "Hello World",
# автором "Telegraph API",
# ссылкой на автора и HTML содержимым.
response = telegraph.create_page(
    title='My name is Pie-Rise The Sound!',
    author_name='Pie-Rise The Sound',
    author_url='https://example.com',
    html_content='<p>I am bear...</p>'
)
# Выводим URL созданной страницы
print(response['url'])