#!/usr/bin/env python

import re
import argparse
import distance
import requests

# 0 = Title
# 1 = Author
# 2 = Publication date
# 3 = Genres

def split_items(f):
	words = []

	lines = f.readlines()

	for line in lines:
		v = re.split("\t", line) 

		words.extend([v])
	return words

def extract_features(items):
	features = []

	for i in range(len(items)):
		values = []
		# title
		values.append(items[i][2])
		# author
		values.append(items[i][3])
		# year of publication
		values.append(items[i][4])

		# split for '"'
		genres = re.split("\"", items[i][5])

		# extract entries starting with a capital
		final_genres =[]
		for genre in genres:
			# if non empty
			if genre:
				# if starting with a capital letter
				if(genre[0].isupper()):
					final_genres.append(genre)

		# genres
		values.append(final_genres)

		# append item features
		features.append(values)

	return features

def pretty_print(data):
	for entry in data:
		print(entry)

# 'K\\u00fcnstlerroman' = Kunstlerroman
# 'Roman \\u00e0 clef' = Roman a clef
def collect_genres(data):
	genres = []
	for entry in data:
		for genre in entry[3]:
			if genre not in genres:
				genres.append(genre)

	return genres


def isbn_lookup(ISBN, KEY):
	url = 'https://isbndb.com/api/books.xml?access_key=' + KEY + '&results=texts&index1=isbn&value1=' + ISBN
	page = requests.get(url)
	print page.text

# commandline argument dataset
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-c", "--corpus", dest = "file")
args = parser.parse_args()

# open and read file
f = open(args.file, "r")

items = split_items(f)

data = extract_features(items)

genres = collect_genres(data)

# pretty_print(data)
# print genres
# print len(genres)

# print(distance.levenshtein("Speculative fiction", "Utopian and dystopian fiction"))

KEY = 'UEE4J4KA'
ISBN = '8495501090'
isbn_lookup(ISBN, KEY)






