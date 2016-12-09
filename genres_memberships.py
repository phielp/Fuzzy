import datetime
# Parse the file with the genres and calculate memberships from 0 to 1 to each genre
def calculate_genre_memberships():
    t = open('books_with_genres.csv', 'r')
    new_file = open('membership_of_genres.csv', 'w')

    starttime = datetime.datetime.now()

    line = t.readline()
    while line:
        # preprocessing of the line to extract the data
        total_num_of_people = 0
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
                num_people = int(''.join([i for i in elements[0] if i.isdigit()]))
                total_num_of_people += num_people
        # one person describes a book with 3 genres on average, that's why it's total_num_of_people/3
        normalizator = total_num_of_people / 3.0
        # for each genre, normalize the value (make it between 0 and 1)
        for genre in genres_list:
            elements = genre.split()
            if elements:
                num_people = int(''.join([i for i in elements[0] if i.isdigit()]))
                genre_name = elements[-1].strip(']').strip('"')
                new_line.append((genre_name, min(1, round(num_people/normalizator, 2))))
        new_file.write(str(isbn) +';' + str(new_line) + '\n')
        line = t.readline()
    print datetime.datetime.now() - starttime

if __name__ == '__main__':
    calculate_genre_memberships()
