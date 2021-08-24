from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/30367563/articles/19449?query=&menuId=75&boardType=L&useCafeId=true&requestFrom=A')
soup = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')

p = re.compile('이름.*n')
text_soup = soup.get_text()
print(text_soup)
m = p.search(text_soup)
print(m.group())
