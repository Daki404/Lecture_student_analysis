from selenium import webdriver
from urllib import parse
import time


def redirect_url(url):
    salt = 'https://cafe.naver.com/studentcodingcamp?iframe_url_='
    url = url.replace('https://cafe.naver.com', '')
    return_url = salt + parse.quote(url, encoding='CP949')
    return return_url


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)

url = 'https://cafe.naver.com/ArticleRead.nhn?clubid=30367563&page=1&menuid=75&boardtype=L&articleid=19437&referrerAllArticles=false'
print(redirect_url(url))
print('https://cafe.naver.com/studentcodingcamp?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D30367563%2526page%3D1%2526menuid%3D75%2526boardtype%3DL%2526articleid%3D19437%2526referrerAllArticles%3Dfalse')
'''
driver.get(redirect_url(url))
time.sleep(3)
print(driver.page_source)
'''