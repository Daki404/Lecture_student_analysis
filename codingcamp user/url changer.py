from urllib import parse

url = 'ArticleRead.nhn?clubid=30367563&page=1&menuid=75&boardtype=L&articleid=19437&referrerAllArticles=false'

tmp = parse.quote(url)

print(tmp)
print('ArticleRead.nhn%253Fclubid%3D30367563%2526page%3D1%2526menuid%3D75%2526boardtype%3DL%2526articleid%3D19437%2526referrerAllArticles%3Dfalse')
print('ArticleRead.nhn%3Fclubid%3D30367563%26page%3D1%26menuid%3D75%26boardtype%3DL%26articleid%3D19437%26referrerAllArticles%3Dfalse%7E')
print('정답', 'https://cafe.naver.com/studentcodingcamp?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D30367563%2526page%3D1%2526menuid%3D75%2526boardtype%3DL%2526articleid%3D19437%2526referrerAllArticles%3Dfalse')
print('java', 'https%3A%2F%2Fcafe.naver.com%2Fstudentcodingcamp.cafe%3Fiframe_url%3D%252FArticleRead.nhn%253Fclubid%253D30367563%2526page%253D1%2526menuid%253D75%2526boardtype%253DL%2526articleid%253D19437%2526referrerAllArticles%253Dfalse')
print('java 반변조','https://cafe.naver.com/studentcodingcamp?iframe_url_utf8='+ '%2FArticleRead.nhn%3Fclubid%3D30367563%26page%3D1%26menuid%3D75%26boardtype%3DL%26articleid%3D20532%26referrerAllArticles%3Dfalse')
