from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def preprocess_sentence_kr(text: str) -> str:
    '''text의 다중공백을 삭제하고, return.'''
    text = text.strip()
    text = re.sub(r"[^a-zA-Z0-9가-힣?!¿]+", " ", text)  # \n도 공백으로 대체해줌
    text = text.strip()
    return text


def soup_maker(post_num: str) -> BeautifulSoup:
    '''query요청에 쓰는 post_num을 이용하여 url생성 후 soup변환.'''
    url = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/30367563/articles/' + post_num + '?query=&menuId=75&boardType=L&useCafeId=true&requestFrom=A'
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser', from_encoding='ANSI')
    return soup


def hash_tag_parser(text: list) -> str:
    print(text)
    return_text = ''
    blank = False

    for i in range(len(text)):
        if (word := text[i]):
            if blank:
                return_text += ' '
                blank = False
            return_text += word
        else:
            blank = True


def soup_parser(soup: BeautifulSoup, arr=[]) -> list:
    '''정규표현식을 이용하여 soup parsing.'''
    pattern = re.compile('이름.*cus')
    text_soup = soup.get_text()

    info_text = pattern.search(text_soup).group()
    info_text = info_text.split('-')

    info_text = [preprocess_sentence_kr(i) for i in info_text]

    for i in range(0, 3):
        arr.append(info_text[i][3:])
    arr.append(info_text[3][19:])
    arr.append(info_text[4][20:])
    arr.append(info_text[5][17:-16])

    return arr


if __name__ == "__main__":
    soup = soup_maker('18477')
    tmp = soup_parser(soup)
    print(tmp)