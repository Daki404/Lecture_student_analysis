from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import url_test

html = urlopen('https://cafe.naver.com/ArticleList.nhn?search.clubid=30367563&search.menuid=75&search.boardtype=L')
soup = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')

tmp = soup.find(class_='prev-next')
print(tmp)

p = re.compile('"/Article.*"')
result = p.findall(str(tmp))


for i in result:
    print(i)

url = 'https://cafe.naver.com/studentcodingcamp?iframe_url=/ArticleList.nhn%3Fsearch.clubid=30367563%26search.menuid=75%26search.boardtype=L%26search.totalCount=151%26search.cafeId=30367563%26search.page=2'
print(url)

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')


