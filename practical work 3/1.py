import requests as req
import bs4 as BeautifulSoup
import pandas as pd

link = "https://smart-lab.ru/q/shares/"
response = req.get(link)
# Былоа просто soup = BeautifulSoup(response.text,'lxml')
# Для коректоной работы, нужно докачивать через pip ещё и lxml
# pip install lxml
soup = BeautifulSoup.BeautifulSoup(response.text,'lxml')
tables = soup.find_all('table')
dfs = pd.read_html(str(tables), index_col=0)
print(dfs)