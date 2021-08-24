from post_num_parser import make_url
import post_num_parser as post_parser
import post_content_parser as content_parser
import matplotlib.pyplot as plt
import seaborn as sns
import re

user_name = []
user_major = []
user_id = []
user_tag = []
user_aim = []
user_letter = []

p = re.compile('[0-9]+')


def parse_page(url=None):
    if url is None:
        post_num = post_parser.post_parse()
    else:

        post_num = post_parser.post_parse(url)

    if post_num:
        for i in post_num:
            try:
                soup = content_parser.soup_maker(i)
                tmp = content_parser.soup_parser(soup)
                user_name.append(tmp[0])
                user_major.append(tmp[1])
                new = p.search(tmp[2]).group()
                if len(new) == 2:
                    user_id.append(new)
                elif len(new) == 4:
                    user_id.append(new[-2:])
                elif len(new) == 8:
                    user_id.append(new[2:4])


                user_tag.append(tmp[3])
                user_aim.append(tmp[4])
                user_letter.append(tmp[5])
            except:
                user_name.append('')
                user_major.append('')
                user_id.append('')
                user_tag.append('')
                user_aim.append('')
                user_letter.append('')
        return True
    else:
        return False


parse_page()
page_num = 2

while True:
    url = make_url(page_num)
    if not parse_page(url):
        break
    page_num += 1

ax = plt.subplots()
ax = sns.countplot(user_id)

plt.show()