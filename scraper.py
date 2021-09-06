import requests
from bs4 import BeautifulSoup

url = "https://sea.ign.com/article/news"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
news = soup.find_all('article', class_='article NEWS')

# Return time, title and description of 5 news articles
for i in range(5):
    print(news[i].get_text())