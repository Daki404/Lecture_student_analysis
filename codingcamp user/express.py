from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/30367563/articles/19492?query=&menuId=75&boardType=L&useCafeId=true&requestFrom=A')
soup = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')

p = re.compile('이름.*cus')
text_soup = soup.get_text()
print(text_soup)
info_text = p.search(text_soup).group()
info_text = info_text.split('-')

print(info_text)

def preprocess_sentence_kr(w):
  w = w.strip()
  w = re.sub(r"[^a-zA-Z0-9가-힣?.!,¿]+", " ", w) # \n도 공백으로 대체해줌
  w = w.strip()
  return w


info_text = [preprocess_sentence_kr(i) for i in info_text]


def info_print(text):
    for i in range(0, 3):
        print(text[i][3:])
    print(text[3][19:])
    print(text[4][20:])
    print(info_text[-1][:-18])


info_print(info_text)