# the parameters that the script takes is the starting index (from where to scrape)
# and the number of books to scrape at once
import requests
import traceback
import time
import sys
from lxml import html
import datetime


def scrape_genres(start_index, number_of_books_at_once):
    # open the file with the books for reading, and a new one to write the scraped info
    t = open('BX-Books.csv', 'r')
    filename = 'books_with_genres' + str(start_index) + '.csv'
    new_file = open(filename, 'w')
    t.readline()
    starttime = datetime.datetime.now()
    # the scrip will be started more than once, so that we have to first navigate to the start_index
    for j in range(start_index):
        t.readline()
    for i in range(start_index, start_index+number_of_books_at_once):
        # try/except is used because we want in any kind of mistake (network or keyboard interrupt
        # for example) to save the sata we have scraped so far
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
            # limit the number of genres to 5, because otherwise we have a lot of books
            # with very low membership degree to a certain genre
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
    print datetime.datetime.now() - starttime

if __name__ == '__main__':
    scrape_genres(int(sys.argv[1]), int(sys.argv[2]))
