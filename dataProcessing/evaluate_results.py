from recommend import give_similar_users, recommend, extract_book_titles
import datetime
import sys

test_data = open('../data/test_data.csv')
training_data = open('../data/training_data.csv')
start_time = datetime.datetime.now()

def read_memberships_file():
	books_with_genres_file = open('../data/membership_of_genres.csv', 'r')
	line = books_with_genres_file	.readline()
	books_with_genres_dict = {}
	while line:
		elements = line.split(';')
		if len(elements) > 1:
			isbn = elements[0]
			genres = dict(eval(elements[1]))
		books_with_genres_dict[isbn] = genres
		line = books_with_genres_file.readline()
	return books_with_genres_dict

books_with_genres_dict = read_memberships_file()

def evaluation_per_user(line):
	number_of_matches = 0
	number_of_mismatches = 0

	elems = line.split(';')
	test_user_input = dict(eval(elems[1]))

	if not len(test_user_input)==0:
		most_preferred_user_genre = max(test_user_input, key=test_user_input.get)
	else:
		most_preferred_user_genre = None
	preferred_genres = [genre for genre in test_user_input if test_user_input[genre] > 5]

	recommendations = recommend(evaluate(test_user_input))

	for book in books_with_genres_dict:
			if book in recommendations:
				if most_preferred_user_genre in books_with_genres_dict[book]:
					number_of_matches += 1
				elif most_preferred_user_genre ==None:
					pass
				elif len([val for val in preferred_genres if val in books_with_genres_dict[book]]) > 0:
					number_of_matches += 1
				else:
					number_of_mismatches += 1
	return (number_of_matches, number_of_mismatches)


def evaluate_test_data(start_index, number_of_users):
	number_of_matches = 0
	number_of_mismatches = 0

	line = test_data.readline()
	for i in range(start_index):
		line = test_data.readline()
	# while line:
	for j in range(number_of_users):
		a, b = evaluation_per_user(line)
		number_of_matches += a
		number_of_mismatches += b
		line = test_data.readline()
	success_rate = number_of_matches / ((number_of_matches + number_of_mismatches)*1.0)
	print datetime.datetime.now() - start_time
	return success_rate

if __name__ == '__main__':
	start_index = int(sys.argv[1])
	number_of_users = int(sys.argv[2])
	print evaluate_test_data(start_index, number_of_users)
