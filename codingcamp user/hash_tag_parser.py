import re


def preprocess_sentence_kr(text: str) -> str:
    '''text의 다중공백을 삭제하고, return.'''
    text = text.strip()
    text = re.sub(r"[^a-zA-Z0-9가-힣?.!,¿]+", " ", text)  # \n도 공백으로 대체해줌
    text = text.strip()
    return text


text= '#열정#사랑#죽음'
text2 = '#열정 #사랑 #죽음'

info_text = [preprocess_sentence_kr(i) for i in text]
info_text2 = [preprocess_sentence_kr(i) for i in text2]
print(info_text)
print(info_text2)

print()


def hash_tag_maker(text: list) -> str:
    return_text = ''
    blank = False

    for i in range(1, len(text)):
        if (word := text[i]):
            if blank:
                return_text += ' '
                blank = False
            return_text += word
        else:
            blank = True

    return return_text


print(hash_tag_maker(info_text))
print(hash_tag_maker(info_text2))

