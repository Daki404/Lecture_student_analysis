from post_num_parser import make_url
import post_num_parser as post_parser
import post_content_parser as content_parser
import re


user_name = []
user_major = []
user_id = []
user_tag = []
user_aim = []
user_letter = []


def id_data_mask(num):
    p = re.compile('[0-9]+')
    new = p.search(num).group().strip()
    if len(new) == 2:
        new = new
    elif len(new) == 4 or len(new) == 8:
        new = new[2:4]
    else:
        return False
    if 10 <= int(new) <= 21:
        return new
    return False


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
                if (st_id := id_data_mask(tmp[2])):
                    user_id.append(int(st_id))
                user_tag.append(tmp[3])
                user_aim.append(tmp[4])
                user_letter.append(tmp[5])
            except:
                pass
        return True
    else:
        return False


def data_parsing():
    parse_page()
    page_num = 2

    while True:
        url = make_url(page_num)
        if not parse_page(url):
            break
        page_num += 1

    return user_name, user_id, user_major, user_tag, user_aim, user_letter



