def give_similar_users(user_input):
	# user_similarities {userID:error}
	users_similarities = {}
	print user_input
	preference = open('../data/training_data.csv','r')
	line = preference.readline()
	elems = line.split(';')
	userID = elems[0]
	preferences = dict(eval(elems[1]))
	similar_users = []
	if not len(user_input)==0:
		most_preferred_user_genre = max(user_input, key=user_input.get)
	else:
		most_preferred_user_genre = None

	while line:
		number_of_matches = 0
		accumulated_error = 0
		for genre in user_input:
			if genre in preferences:
				accumulated_error += abs(preferences[genre] - user_input[genre])
				number_of_matches += 1
				matched_genre = genre
		if number_of_matches == 0:
			error = 9
		elif number_of_matches == len(user_input) and accumulated_error < 2:
			error = -1
		elif number_of_matches == 1 and matched_genre == most_preferred_user_genre:
			error = accumulated_error - 2
		else:
			error = accumulated_error / (number_of_matches * 1.0)
		users_similarities[userID] = error
		elems = line.split(';')
		userID = elems[0]
		preferences = dict(eval(elems[1]))
		line = preference.readline()

	for i in range(10):
		mini = min(users_similarities, key=users_similarities.get)
		similar_users.append(mini)
		#print users_similarities[mini]
		del users_similarities[mini]
	#print similar_users
	return similar_users

def recommend(similar_users):
	ratings = open('../data/new_user_ratings_no_zeroes.csv')
	recommended_books = []
	line = ratings.readline()
	while line:
		elems = line.split(';')
		userID = elems[0].strip('"')
		isbn = elems[1].strip('"')
		rating = int(''.join([i for i in elems[2] if i.isdigit()]))
		counter = 0

		if userID in similar_users and rating > 8:
			if isbn not in recommended_books and counter < 2:
				recommended_books.append(isbn)
				counter += 1
		if len(recommended_books) == 5:
			return recommended_books

		line = ratings.readline()
	#print recommended_books
	return recommended_books

def extract_book_titles(recommended_books):
	books = open('../data/BX-Books.csv')
	line = books.readline()
	titles = []

	while line:
		line = books.readline()
		elems = line.split(';')
		if len(elems) > 1:
			isbn = elems[0].strip('"')
			title = elems[1].strip('"')

		if isbn in recommended_books:
			titles.append(title)
	return titles



# prints the userID and the error value of the similaritie between the users
#user_input = {"'drama'": 1, "'comedy'": 10, "'fiction'": 8}
#users = give_similar_users(user_input)
#print extract_book_titles(recommend(users))
#print users
#print recommend(users)
