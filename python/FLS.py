# run command in matlab to start connection:
#
# 		matlab.engine.shareEngine
#

# https://nl.mathworks.com/help/matlab/matlab-engine-for-python.html
import matlab.engine

# open connection with MATLAB
engine = matlab.engine.connect_matlab()

# open dataset
user_ratings = open('data/new_ratings.csv','r')

# main
def FLS(n):
	# iterate first n users
	for i in range(n):
		line = user_ratings.readline()

		elems = line.split(';')
		userID = int(elems[0])
		rest = eval(elems[1])
		userAge = int(rest[0])
		ratedBooks = rest[1]

		final = getOutput(ratedBooks)


# call MATLAB Fuzzy Toolbox
def fuzzyMatlab(rating, member):
	result = engine.FLS(rating, member)
	return result

# return crisp output of FLS
def getOutput(ratedBooks):
	output = []
	print "Rated Books 1 user: ", ratedBooks

	for i in range(len(ratedBooks)):
		isbn, rating = ratedBooks[i]
		rating = float(rating)
		genres = getGenreMembers(isbn)

		results = []
		if genres is not None:
			print "Genre member: ", isbn, genres

			for j in range(len(genres)):
				genre, member = genres[j]
				member = float(member)
				results.append(fuzzyMatlab(rating,member))
			output.append(results)

	print "FLS output: ", output

	return output

# get a list of genre memberships for a book
def getGenreMembers(isbn):
	# open isb lookup (genre meberships)
	genre_members = open('data/membership_of_genres.csv','r')

	for number, line in enumerate(genre_members, 0):
		if isbn in line:
			elems = line.split(';')
			genres = eval(elems[1])
			genre_members.close()
			return genres

# main
FLS(10)

# close connection with MATLAB
engine.quit()


