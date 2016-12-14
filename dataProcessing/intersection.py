ratings = open('BX-Book-Ratings.csv', 'r')
genres = open('books_with_genres.csv', 'r')
new_file = open("new_user_ratings.csv", 'w')
books = []
line = genres.readline()
while line:
    isbn = line.split(';')[1]
    books.append(isbn)
    line = genres.readline()

line2 = ratings.readline()
i = 0
while line2:
    i+=1
    if i % 1000 == 0:
        print i
    try:
        line2 = ratings.readline()
        isbn = line2.split(';')[1].strip('"')
        if isbn in books:
            new_file.write(line2)
    except Exception:
        new_file.close()
        ratings.close()
        genres.close()
