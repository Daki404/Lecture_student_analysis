from urllib.request import urlopen
import requests

url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=30367563&search.menuid=75&search.boardtype=L'
html = requests.get(url).text

with open('cafe.txt', 'w', encoding='utf-8') as f:
    f.write(html)