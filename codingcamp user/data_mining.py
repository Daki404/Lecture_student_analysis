import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import seaborn as sns
import data_maker


def draw_id(user_id):
    fm.get_fontconfig_fonts()
    font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
    font_name = fm.FontProperties(fname=font_location).get_name()
    plt.rc('font', family=font_name)

    sns.set(font="NanumGothic", style='darkgrid')

    plt.subplots()
    #plt.xticks(range(10, 22))
    sns.countplot(user_id)
    plt.xlabel('Code it! 수강생 학번')
    plt.savefig('수강생 학번')


user_name, user_id, user_major, user_tag, user_aim, user_letter = data_maker.data_parsing()

with open('major.txt', 'w', encoding='UTF-8') as f:
    f.write(' '.join(user_major))

with open('tag.txt', 'w', encoding='UTF-8') as f:
    f.write(' '.join(user_tag))

with open('aim.txt', 'w', encoding='UTF-8') as f:
    f.write(' '.join(user_aim))

with open('letter.txt', 'w', encoding='UTF-8') as f:
    f.write(' '.join(user_letter))

draw_id(user_id)