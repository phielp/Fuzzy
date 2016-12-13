ratings = open('new_user_ratings.csv', 'r')
new_file = open("new_user_ratings_no_zeroes.csv", 'w')

line = ratings.readline()
while line:
    elems = line.split(';')
    if elems:
        rating = int(''.join([i for i in elems[2] if i.isdigit()]))
        if int(rating) != 0:
            new_file.write(line)
        line = ratings.readline()

