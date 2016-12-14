# run command in matlab to start connection:
#
# 		matlab.engine.shareEngine
#

# https://nl.mathworks.com/help/matlab/matlab-engine-for-python.html
import matlab.engine
import operator

# open connection with MATLAB
engine = matlab.engine.connect_matlab()

# open dataset
user_ratings = open('../data/new_ratings.csv','r')
# new_file = open('../data/user_preferences.csv','w')

# main
def FLS(n):
	
	# line = user_ratings.readline()
	count = 0

	for i in range(n):
		line = user_ratings.readline()
		elems = line.split(';')
		userID = int(elems[0])
		rest = eval(elems[1])
		userAge = int(rest[0])
		ratedBooks = rest[1]

		preference = getUserPrefrence(ratedBooks)

		# preftext = str(preference)
		# text = str(userID) + ';' + preftext + '\n'

		# new_file.write(text)
		# line = user_ratings.readline()
		# if count % 500 == 0:
		# 	print count
		# count += 1

		print userID, preference
		print '\n'

# call MATLAB Fuzzy Toolbox
def fuzzyMatlab(rating, member):
	result = engine.FLS(rating, member)
	return result

# return user preferences in order of liking
def getUserPrefrence(ratedBooks):

	preferences = {}
	genreCounts = {}
	for i in range(len(ratedBooks)):
		isbn, rating = ratedBooks[i]
		rating = float(rating)
		genres = getGenreMembers(isbn)

		# if there is genre information in data
		if genres is not None:

			# calculate weight per genre
			for j in range(len(genres)):
				genre, member = genres[j]
				member = float(member)

				# add weights together if genre exists in preferences
				if genre in preferences:
					preferences[genre] += fuzzyMatlab(rating,member)
					genreCounts[genre] += 1
				else:
					preferences[genre] = fuzzyMatlab(rating,member)
					genreCounts[genre] = 1

	# normalize for recurring genres
	for key, value in preferences.iteritems():
		normal = genreCounts[key]
		preferences[key] = value / normal

	# sort list
	sortedPreferences = sorted(preferences.items(), key=operator.itemgetter(1), reverse=True)

	return sortedPreferences

# get a list of genre memberships for a book
def getGenreMembers(isbn):
	genre_members = open('../data/membership_of_genres.csv','r')

	for number, line in enumerate(genre_members, 0):
		if isbn in line:
			elems = line.split(';')
			genres = eval(elems[1])
			genre_members.close()
			return genres

# makes a list of all different genres in the data
def createGenreSet():
	genre_members = open('../data/membership_of_genres.csv','r')
	allGenres = []
	allGenres = set(allGenres)
	line = genre_members.readline()
	while line:
		elems = line.split(';')
		genres = eval(elems[1])
		for i in range(len(genres)):
			genre, member = genres[i]
			if member not in allGenres:
				allGenres.add(genre)
		
		line = genre_members.readline()
	genre_members.close()
	return allGenres
	
# main
FLS(7)

# close connection with MATLAB
engine.quit()


