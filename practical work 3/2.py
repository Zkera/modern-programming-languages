import requests as req
import bs4 as BeautifulSoup

link = "http://esimo.ru/portal/"
response = req.get(link)
soup = BeautifulSoup.BeautifulSoup(response.text,'lxml')
images = soup.find_all('img')
for item in images:
    print(item['src'])