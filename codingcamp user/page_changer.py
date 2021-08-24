import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


def make_url(page_num: int) -> BeautifulSoup:
    session = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=30367563&search.menuid=75&search.boardtype=L&search.totalCount=151&search.cafeId=30367563&search.page=' + str(page_num)

    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')
    return soup
    '''
    req = session.get(url, headers=headers)
    #print(url)
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs
'''


if __name__ == "__main__":
    print(make_url(2))
