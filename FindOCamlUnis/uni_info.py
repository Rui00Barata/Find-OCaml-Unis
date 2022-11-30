from bs4 import BeautifulSoup

import webpage
import uni_results

url = "https://www.4icu.org/us/a-z/"
uni_rank = webpage.get_html(url)
uni_rank = BeautifulSoup(uni_rank, "html.parser")

uni_list = uni_rank.tbody


def filter_uni_list():
    global uni_list

    uni_list = uni_list[(uni_list.index("/reviews/5809.htm")+1):]


with open('uni_list.txt', 'a') as f:

    uni_list = uni_list.find_all('a')
    uni_list = list(map((lambda tag: tag.get('href')), uni_list))

    # filter_uni_list()

    for link in uni_list:

        url = "https://www.4icu.org" + link

        if (uni_results.has_results(url)):
            print(True)
            f.write(url)
            f.write('\n')
        else:
            print(False)
