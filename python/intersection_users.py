users = open('BX-Users.csv', 'r')
ratings = open('new_user_ratings_no_zeroes.csv', 'r')
new_file = open("new_users.csv", 'w')
users_arr = []
line = ratings.readline()
while line:
    user_id = int(''.join([i for i in line.split(';')[0] if i.isdigit()]))
    users_arr.append(user_id)
    line = ratings.readline()

line2 = users.readline()
i = 0
while line2:
    i+=1
    if i % 1000 == 0:
        print i
    try:
        line2 = users.readline()
        user_id = int(line2.split(';')[0].strip('"'))
        if user_id in users_arr:
            new_file.write(line2)
    except Exception:
        new_file.close()
        users.close()
        ratings.close()
        break
