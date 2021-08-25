from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "파이썬 워드클라우드 파이썬 좋아 워드클라우드 파이썬 라이브러리 좋아 파이썬 워드클라우드 예시 워드클라우드 우한 폐렴 조심 데이터 분석 우한 워드클라우드 중국 박쥐 감염 코로나바이러스"

wordcloud = WordCloud(font_path='font/NanumGothic.ttf', background_color='white').generate(text)

plt.figure(figsize=(7, 7))
plt.imshow(wordcloud, interpolation='lanczos')
plt.axis('off')
plt.show()