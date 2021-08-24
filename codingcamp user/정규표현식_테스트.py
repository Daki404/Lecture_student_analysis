from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

p = re.compile('몰라')
text = '안녕 니 이름은 뭐야? 몰라 멍청아'
print(text)
m = re.match('몰라', text)
print(m)
