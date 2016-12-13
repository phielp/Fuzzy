import re

# Creates a table with one user per row:
# user-ID, age
def createUserTable(users, ratings):
	table = dict()
	line = users.readline()
	while line:
		words = re.split(';', line)
		# Get user-ID and save as int
		userID = int(words[0].strip('"'))


		# Get user age and save as int
		# If there is no age info put 0
		try:
			digit = ''.join([i for i in words[2] if i.isdigit()])
			if digit:
				userAge = int(digit)
			else:
				userAge = 0
		except IndexError:
			return None

		table[userID] = userAge
		line = users.readline()

	return table

# Creates a table with Unique user-ID's followed by
# an arbitrary number of (isbn, rating)-tuples
def createRatingsTable(ratings):
	table = dict()
	line = ratings.readline()
	words = re.split(';', line)
	currentUserID = int(words[0].strip('"'))
	arrayOfRatings = []

	isbn = (words[1].strip('"'))
	digit = ''.join([i for i in words[2] if i.isdigit()])
	rating = int(digit)
	entry = (isbn, rating)

	arrayOfRatings.append(entry)

	while line:
		words = re.split(';', line)

		# Get user-ID and store if new user-ID
		newUserID = int(words[0].strip('"'))
		if currentUserID != newUserID:
			table[currentUserID] = arrayOfRatings
			arrayOfRatings = []
			currentUserID = newUserID

		# Get (isbn, rating) for one entry
		isbn = (words[1].strip('"'))
		digit = ''.join([i for i in words[2] if i.isdigit()])
		rating = int(digit)
		entry = (isbn, rating)

		arrayOfRatings.append(entry)
		line = ratings.readline()

	return table

# Creates a combined user and ratings table
def mergeTables(userTable, ratingTable):
	table = dict()

	for user in userTable:
		entry = []

		# Copy user-ID and age
		entry.append(userTable[user])

		# Copy (isbn, rating)-tuples as list
		if user in ratingTable:
			entry.append(ratingTable[user])

		table[user] = entry

	return table

def pretty_print(data):
	for entry in data:
		print(entry)

########### MAIN ############

# Open files
# Delete column headers in csv-files!
users = open('new_users.csv', 'r')
ratings = open('new_user_ratings_no_zeroes.csv', 'r')
new_file = open('new_ratings.csv', 'w')

ratingTable = createRatingsTable(ratings)

userTable = createUserTable(users, ratings)

finalTable = mergeTables(userTable, ratingTable)

for line in finalTable:
	new_file.write(str(line) + ';' + str(finalTable[line]) + '\n')

# pretty_print(finalTable)

users.close()
ratings.close()
