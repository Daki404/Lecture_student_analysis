from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import url_test

url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=30367563&search.menuid=75&search.boardtype=L'

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')
print(soup)
tmp = soup.find(class_='prev-next')


p = re.compile('"/Article.*"')
result = p.findall(str(tmp))


for i in result:
    print(i)
print()

#url = 'https://cafe.naver.com/studentcodingcamp?iframe_url=/ArticleList.nhn%3Fsearch.clubid=30367563%26search.menuid=75%26search.boardtype=L%26search.totalCount=151%26search.cafeId=30367563%26search.page=2'

