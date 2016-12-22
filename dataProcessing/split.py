data = open('../data/user_preferences.csv', 'r')
test = open('../data/test_data.csv', 'w')
training = open('../data/training_data.csv', 'w')

line = data.readline()
i = 0
while line:
	i += 1
	if i < 15000:
		test.write(line)
	else:
		training.write(line)
	line = data.readline()
