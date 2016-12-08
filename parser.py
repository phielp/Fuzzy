# coding: utf-8
# f = open('booksummaries.txt', 'r')
# books1 = []
# books2 = []
# t = open('BX-Books.csv', 'r')
# line = f.readline()
# while line:
#     els = line.split('\t')
#     books1.append(els[2])
#     line = f.readline()

# line = t.readline()
# while line:
#     els = line.split(';')
#     books2.append(els[2].strip('"'))
#     line = t.readline()
# #print len([book for book in books1 if book in books2])

import requests
import sys
import traceback
import time
from lxml import html
import datetime
import xml.etree.ElementTree as ElementTree
reload(sys)
sys.setdefaultencoding('utf-8')

START_INDEX = 7504
NUMBER_OF_BOOKS_AT_ONCE = 10000

t = open('BX-Books.csv', 'r')
new_file = open('books_with_genres3.csv', 'w')
t.readline()
starttime = datetime.datetime.now()
for j in range(START_INDEX):
    t.readline()
for i in range(START_INDEX, START_INDEX+NUMBER_OF_BOOKS_AT_ONCE):
    try:
        line = t.readline()
        els = line.split(';')
        isbn = els[0].strip('"')
        url = "https://www.goodreads.com/search?q=" + isbn
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        page = requests.get(url, headers=headers)
        root = html.document_fromstring(page.text)
        #e = root.xpath('.//a[@class="actionLinkLite bookPageGenreLink"]')
        genresList = root.xpath('.//a[@class="actionLinkLite greyText bookPageGenreLink"]')
        etexts = [ei.attrib['title'] for ei in genresList]
        if len(etexts) > 5:
            while len(etexts) > 5:
                del etexts[5]
        newline = str(i) + ';' + str(isbn) + ';' + str(etexts) + '\n'
        new_file.write(newline)
        time.sleep(0.1)
    except Exception:
        print datetime.datetime.now() - starttime
        print i
        traceback.print_exc()
        t.close()
        new_file.close()
        sys.exit()

# f = open('a.html', 'w')
# f.write(page.text)


# etexts = [ei.text for ei in e]
# genres = set(etexts)
# print genres

print datetime.datetime.now() - starttime
