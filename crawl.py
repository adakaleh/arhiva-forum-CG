# -*- coding: utf-8 -*-

# RUN WITH:
# [torsocks] python3 crawl.py

# Helpful:
#   https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#   https://www.dataquest.io/blog/web-scraping-tutorial-python/
#   https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

# for making HTTP requests
import requests

# for sending POST data
import json

# for parsing webpages
from bs4 import BeautifulSoup

# for delays between requests
from time import sleep

# for writing to file
import os


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': "application/x-www-form-urlencoded",
}
login_data = {
    'vb_login_username': 'arhivist',
    'vb_login_password': 'f4n3gonws',
    'vb_login_password_hint': 'Password',
    'cookieuser': '1',
    's': '',
    'securitytoken': 'guest',
    'do': 'login',
    'vb_login_md5password': '',
    'vb_login_md5password_utf': ''
}

# start session in which cookies will be saved
req = requests.Session()

# login
page = req.post('http://forum.computergames.ro/login.php?do=login', data=login_data, headers=headers)

# (if no login) get cookies first, so that there's no "sid" parameter in all urls
#page = req.get('http://forum.computergames.ro/external.php?type=RSS2', headers=headers)

sleep(1)


# get URLs
urls_file = open('lists/members_only.txt', 'r')

for url in urls_file:

    # strip the newline at the end of the url string
    url = url.rstrip()

    all_links = "http://forum.computergames.ro/external.php?type=RSS2\n"
    all_links += "http://forum.computergames.ro/\n"

    # get page
    page = req.get(url, headers=headers)

    #print(page.status_code)
    #print(page.content)

    soup = BeautifulSoup(page.content, 'html.parser')

    # TODO: go to the next page in the (sub-)forum
    # get number of pages in the current forum
    forum_pages = soup.find_all('a', class_='popupctrl')
    #fp = soup.select('.threadpagenav .popupctrl');
    #if len(fp):
    #    fp_text = fp[0].get_text().partition('of ')[2]
    #    if fp_text != '':
    #        forum_pages = int(fp_text)

    print('=== ' + url + ' ===')
    print('=== ' + str(forum_pages) + ' ===')

    for forum_page in range(1, forum_pages + 1):
        current_forum_page = url
        if forum_page != 1:
            current_forum_page = url[:-5] + '/page-' + str(forum_page) + '.html'

        # get page
        sleep(0.5)
        page = req.get(current_forum_page, headers=headers)

        print(current_forum_page + ' of ' + str(forum_pages))
        print(page.status_code)
        #print(page.content)

        all_links += current_forum_page + "\n"

        soup = BeautifulSoup(page.content, 'html.parser')

        # get threads
        threads = soup.find_all('a', class_='title')

        for thread in threads:
            print(thread['href'])

            # get number of pages
            thread_id = thread['id'].replace('thread_title_', '')
            pagination_element = soup.select('#pagination_threadbit_' + thread_id + ' dt')
            number_of_pages = 1
            #if pagination_element is not None:
            if len(pagination_element):
                #print(pagination_element[0].get_text())
                number_of_pages = int(pagination_element[0].get_text().partition(' ')[0])

            # don't insert duplicates
            if thread['href'] not in all_links:
                all_links += thread['href'] + "\n"

                if number_of_pages > 1:
                    for pg in range(2, number_of_pages + 1):
                        all_links += thread['href'][:-5] + '/page-' + str(pg) + '.html' + "\n"

            #link = thread['href'] + ' ||| ' + thread.get_text() + ' ||| ' + number_of_pages + "\n"


    filename = 'threads__' + url.split('/')[3][:-5] + '.txt'

    # write to file
    os.makedirs('lists', exist_ok=True)
    fo = open('lists/' + filename, 'w')
    fo.write(all_links)
    fo.close()

urls_file.close()

