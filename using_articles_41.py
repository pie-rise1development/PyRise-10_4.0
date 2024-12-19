from newspaper import Article

url = 'https://habr.com/ru/articles/86734/'

article = Article(url)

article.get()
article.parse()

print(article.title)
print(article.text)