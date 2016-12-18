preference = open('../data/user_preferences.csv','r')


def evaluate(user_input):
	# user_similarities {userID:error}
	users_similarities = {}

	line = preference.readline()
	elems = line.split(';')
	userID = elems[0]
	preferences = dict(eval(elems[1]))

	while line:
		number_of_matches = 0
		accumulated_error = 0
		for genre in user_input:
			if genre in preferences:
				accumulated_error += abs(preferences[genre] - user_input[genre])
				number_of_matches += 1
		if number_of_matches == 0:
			error = 9
		else:
			error = accumulated_error / (number_of_matches * 1.0)
		users_similarities[userID] = error
		elems = line.split(';')
		userID = elems[0]
		preferences = dict(eval(elems[1]))
		line = preference.readline()

	for i in range(5):
		mini = min(users_similarities, key=users_similarities.get)
		print mini
		print users_similarities[mini]
		del users_similarities[mini]

# prints the userID and the error value of the similaritie between the users
user_input = {"'drama'": 1, "'comedy'": 10, "'fiction'": 8}
evaluate(user_input)
