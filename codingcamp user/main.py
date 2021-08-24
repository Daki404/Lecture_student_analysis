from post_num_parser import make_url
import post_num_parser as post_parser
import post_content_parser as content_parser


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
                print(tmp)
            except:
                print([''])
        return True
    else:
        return False


parse_page()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

page_num = 2
while True:
    url = make_url(page_num)
    if not parse_page(url):
        break
    page_num += 1
print(page_num)
