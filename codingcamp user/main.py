from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://cafe.naver.com/ArticleList.nhn?search.clubid=30367563&search.menuid=75&search.boardtype=L')
bs = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')

tmp = bs.find_all(class_='article', href=re.compile('.*Articles=false'))
for i in tmp:
    print(i.get('href'))



'''
with open('cafe.txt', 'w', encoding='utf-8') as f:
    for i in tmp:
        print()
        '''