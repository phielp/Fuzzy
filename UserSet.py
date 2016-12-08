import re

# Creates a table with one user per row:
# user-ID, age
def createUserTable(users, ratings):

	userRatings = usersWithRatings(ratings)

	table = []
	lines = users.readlines()
	for line in lines:
		entry = []
		words = re.split(';', line)
		# Get user-ID and save as int
		userID = int(words[0].strip('"'))

		if userID in userRatings:
			entry.append(userID)

			# Get user age and save as int
			# If there is no age info put 0
			try:
				digit = ''.join([i for i in words[2] if i.isdigit()])
				if digit:
					entry.append(int(digit))
				else:
					entry.append(0)
			except IndexError:
				return None

			table.append(entry)

	return table

# Returns list of users who rated at least 1 book
def usersWithRatings(ratings):
	table = []
	lines = ratings.readlines()
	for line in lines:
		words = re.split(';', line)
		table.append(int(words[0].strip('"')))
		aSet = set(table)

		# userID = int(words[0].strip('"'))
		# if userID not in table:
		# 	table.append(userID)

	return list(aSet)

# Creates a table with Unique user-ID's followed by 
# an arbitrary number of (isbn, rating)-tuples
def createRatingsTable(ratings):
	table = []
	lines = ratings.readlines()
	for line in lines:
		words = re.split(';', line)

		# Get user-ID and store if new user-ID
		userID = int(words[0].strip('"'))
		if userID not in table:
			table.append(userID)

		# Get (isbn, rating) for one entry
		isbn = (words[1].strip('"'))
		digit = ''.join([i for i in words[2] if i.isdigit()])
		rating = int(digit)
		entry = (isbn, rating)
		
		table.append(entry)

	return table

# Creates a combined user and ratings table
def mergeTables(userTable, ratingTable):
	table = []
	
	for user in userTable:
		entry = []

		# Copy user-ID and age
		entry.append(user[0])
		entry.append(user[1])

		# Copy (isbn, rating)-tuples as list
		if user[0] in ratingTable:
			index = ratingTable.index(user[0])
			while index+1 < len(ratingTable) and type(ratingTable[index+1]) is tuple:
				entry.append(ratingTable[index+1])
				index += 1

		table.append(entry)

	return table

def pretty_print(data):
	for entry in data:
		print(entry)

########### MAIN ############

# Open files
# Delete column headers in csv-files!
users = open('BX-Users.csv', 'r')
ratings = open('BX-Book-Ratings.csv', 'r')

# userTable = createUserTable(users, ratings)
table = usersWithRatings(ratings)
# print table

# ratings = open('BX-Book-Ratings.csv', 'r')

# ratingTable = createRatingsTable(ratings)

# finalTable = mergeTables(userTable, ratingTable)

# pretty_print(finalTable)

users.close()
ratings.close()
