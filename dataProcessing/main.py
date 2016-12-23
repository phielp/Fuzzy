from recommend import give_similar_users, recommend, extract_book_titles

if __name__ == '__main__':
	membership_file = open('../data/membership_of_genres.csv', 'r')
 	print "Hello. If you want us to recommend you a book, please give a grade from 1 to 10 to the following genres:"
 	user_preferences = {}
 	grade1 = raw_input('fiction: ')
 	user_preferences["'fiction'"] = int(grade1)
 	grade2 = raw_input('non-fiction: ')
 	user_preferences["'non-fiction'"] = int(grade2)
 	all_genres = set()
 	predefined_genres = ['action', 'adventure', 'art', 'biography', 'cartoon', 'chick-lit', 'childrens',
 				'comedy', 'classics', 'crime', 'drama', 'fantasy', 'horror', 'mystery', 'mythology',
 				'mathematics', 'romance', 'science-fiction', 'short-story', 'thriller', 'history', 'religion',
 				'poetry', 'philosophy', 'science']
 	print "Here are some genres that you could choose from and give a grade"
 	for line in membership_file:
 		for genre in dict(eval(line.split(';')[1])):
 			all_genres.add(genre)

 	print sorted(predefined_genres)
 	print "If you want to see the full list of genres, type 'full', otherwise type <genre>*<grade> <newline>."
 	print "when you're done type 'end'"

 	user_input = raw_input()
 	while user_input != 'end':
 		if user_input == 'full':
 			print sorted(all_genres)
 		else:
 			elems = user_input.split('*')
 			user_preferences["'{}'".format(str(elems[0]))] = int(elems[1])
 		user_input = raw_input()
 	#print user_preferences
 	print recommend(give_similar_users(user_preferences))

