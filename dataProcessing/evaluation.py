import distance
import operator
import numpy as np

preference = open('data/user_preferences.csv','r')

# makes a list of all different genres in the data
def createGenreSet():
	genre_members = open('data/membership_of_genres.csv','r')
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

# levenshtein distance between a target genre and all other genres
def calcGenreDistance(allGenres, target):
	distances = {}

	for genre in allGenres:
		distances[genre] = int(distance.levenshtein(genre, target))

	return distances

# create dict with all value for all genres
def addAllGenres(preferences):
	allGenres = createGenreSet()
	result = {}
	for genre in allGenres:
			result[genre] = 0
	for key, value in preferences.iteritems():
		result[key] = preferences[key]

	return result

# return vector of votes for all genres
def returnVector(preferences):
	userPref = addAllGenres(preferences)
	userPref = sorted(userPref.items(), key=operator.itemgetter(0))
	prefVect = np.zeros(len(userPref))

	for i in range(len(userPref)):
		genre, value = userPref[i]
		prefVect[i] = value

	return prefVect

# calculate eucledian distance between 2 vectors
def eucledianDist(X, Y):
	dist = np.linalg.norm(X-Y)
	return dist

# compare users preferences
def evaluation(n):
	line = preference.readline()
	elems = line.split(';')
	userID = elems[0]
	preferences = dict(eval(elems[1]))
	target = returnVector(preferences)

	for i in range(n):
		line = preference.readline()
		elems = line.split(';')
		userID = elems[0]
		preferences = dict(eval(elems[1]))

		prefVect = returnVector(preferences)
		dist = eucledianDist(prefVect, target)
		print dist
	

evaluation(5)




