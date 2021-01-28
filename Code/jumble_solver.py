from __future__ import print_function

import urllib
import os.path
import argparse

from urllib.request import urlopen


##
## Downloads the word list as data set
##
def download():

	#link to the words list dataset
	link = "http://www.mit.edu/~ecprice/wordlist.10000"

	#try to connect to the specified url. Throw an exception on failure
	try:

		#open the link and read the data on the link
		data = urlopen(link)
		words_data = data.read().decode('utf-8')


		#file path to data set (.txt) file
		data_file_path = "./../Data/word_list.txt"

		#Checks if the data set file exists. If not true, will create a new file
		if not os.path.isfile(data_file_path):
			print("Downloading Dataset")

			#opening the file 
			file = open("./../Data/word_list.txt", "w+")
			# f.seek(0)

			#writing the downloaded data to the file
			file.write(words_data)
			# file.truncate()
			print("Dataset Downloaded Successfully")

		#if data file already exists
		else:
			print("Data already exists.All set!")

	#failed to connect to the url
	except:
		print("Problem connecting to the url! Try Again")
		exit()

	
##
## Searchs for the word in the dataset
##
## :param      search_word:  The user deifned word for which we find the match
## :type       search_word:  string
## :param      filename:     The filename which contains a list of english words
## :type       filename:     string
##
def search_word(search_word, file_path='word_list.txt'):

	#try to open the file. Throws an exception if file does not exist

	if file_path == 'word_list.txt':
		dir_path = './../Data/word_list.txt'
	else:
		dir_path = file_path

	try:
		#open the word list file and read it
		file = open(dir_path, "r")
		file_data = file.read().split()
	except:
		print("File does not exist!")
		exit()


	#iterating over every word in the file
	for word in file_data:

		#check if the search word matches the word word in the file. This also #check for anagrams
		if sorted(word) == sorted(search_word):
			print("Original Word Found: ", word)

		#tries to search for substring matches
		search_substring(search_word=search_word, word=word)

def create_aux(word):
    aux = [0] * len(word)

    i = 1
    j = 0
    while i < len(word):
        if word[i] == word[j]:
            j += 1
            aux[i] = j
            i += 1
        
        elif word[i] != word[j] and j != 0:
            j = aux[j-1]
        else:
            aux[i] = 0
            i += 1

    return aux

def search_substring(search_word, word):
	aux = create_aux(word)

	
	i = 0
	
	j = 0
	while j < len(search_word):
	    if word[i] != search_word[j]:
	        if i == 0:
	            j += 1
	        else:
	            i = aux[i-1]
	    else:
	        i += 1
	        j += 1
	        if i == len(word):
	            print("Found substring in word list: ", word)
	            i = aux[i-1]


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	# download_data()

	#read the filename from the user. This is an optional argument 
	#deafult is the already available dataset in ./Data folder
	parser.add_argument('-f', '--filename', help='Word List Filename', required=False, default='word_list.txt')

	#read the user defined word from the cli
	parser.add_argument('-w', '--word', help='Search Word', required=True)

	#read the user input to make a choice on downloading data from the url
	# parser.add_argument('-d', '--download_data', help='Download the data from the link', required=False)

	args = parser.parse_args()

	#user selects to download the dataset
	if args.filename == 'word_list.txt':
		download()

	print("======================================")
	print("Word List filename: ", args.filename)
	print("Word to search for: ", args.word)
	print("======================================")


	# download the data and save it in a text file
	search_word(search_word=args.word, file_path=args.filename)



	
	

	
	

