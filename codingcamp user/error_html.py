from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='chromedriver', options=options)

url = 'https://cafe.naver.com/ArticleRead.nhn?clubid=30367563&page=1&menuid=75&boardtype=L&articleid=19437&referrerAllArticles=false'

driver.get(url)
time.sleep(5)
print(driver.page_source)
driver.close()