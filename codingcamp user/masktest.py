import numpy as np
from PIL import Image
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt

logo_mask = np.array(Image.open('logo.png'))

with open('major'
          '.txt', 'r', encoding='UTF-8') as f:
    text = f.read()

wordcloud = WordCloud(font_path='font/NanumGothic.ttf', background_color='white', mode='RGBA', mask=logo_mask).generate(text)

image_colors = ImageColorGenerator(logo_mask)

plt.figure(figsize=(7, 7))
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='lanczos')
plt.axis('off')
plt.show()
