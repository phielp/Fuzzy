import datetime
# Parse the file with the genres and calculate memberships from 0 to 1 to each genre

t = open('books_with_genres.csv', 'r')
new_file = open('membership_of_genres.csv', 'w')
total_num_of_people = 0

starttime = datetime.datetime.now()

line = t.readline()
while line:
    elems = line.split(';')
    isbn = elems[1]
    genres = elems[2]
    genres = genres.strip('[').strip(']')

    genres_list = genres.split(', ')
    new_line = []

    # count how many people in total rated this book
    for genre in genres_list:
        elements = genre.split()
        # sometimes the list with genres is empty
        if elements:
            # sometimes there is a weird value that looks like 'u"23' that we do not consider
            try:
                num_people = int(elements[0].strip('"'))
            except Exception:
                num_people = 0
            total_num_of_people += num_people
    # one person describes a book with 3 genres on average, that's why it's total_num_of_people/3
    normalizator = total_num_of_people / 3.0
    # for each genre, normalize the value (make it between 0 and 1)
    for genre in genres_list:
        elements = genre.split()
        if elements:
            try:
                num_people = int(elements[0].strip('"'))
            except Exception:
                num_people = 0
            genre_name = elements[-1].strip(']').strip('"')
            new_line.append((genre_name, min(1, round(num_people/normalizator, 2))))
    new_file.write(str(isbn) +';' + str(new_line) + '\n')
    line = t.readline()
print datetime.datetime.now() - starttime
