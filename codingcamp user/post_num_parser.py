from urllib.request import urlopen
from bs4 import BeautifulSoup


def post_parse(url='https://cafe.naver.com/ArticleList.nhn?search.clubid=30367563&search.menuid=75&search.boardtype=L') -> list:
    arr = []
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')

    tmp = bs.find_all(class_='inner_number')

    for i in tmp:
        arr.append(i.text)

    return arr


def make_url(page_num: int) -> str:
    url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=30367563&search.menuid=75&search.boardtype=L&search.totalCount=151&search.cafeId=30367563&search.page=' + str(page_num)
    return url


if __name__ == "__main__":
    print(post_parse())