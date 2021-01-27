from __future__ import print_function

import urllib
import os.path
import argparse

from urllib.request import urlopen


##
##Downloads the word list as data set
##
def download_data():

	#link to the words list dataset
	link = "http://www.mit.edu/~ecprice/wordlist.10000"
	try:
		data = urlopen(link)
		words_data = data.read().decode('utf-8')

		#file path to data set (.txt) file
		data_file_path = "./../Data/word_list.txt"

		#Checks if the data set file exists. If not true, will create a new file
		if not os.path.isfile(data_file_path):
			print("Downloading Dataset")
			file = open("./../Data/word_list.txt", "w+")
			file.write(words_data)
			print("Dataset Downloaded Successfully")

		else:
			print("Data already exists.All set!")
	except:
		print("Problem connecting to the url! Try Again")
		exit()
	
##
## Searchs for the word in the dataset
##
## :param      search_word:  The search word
## :type       search_word:  string
##
def search_word(search_word):

	#open the word list file and read it
	file = open("./../Data/word_list.txt", "r")
	file_data = file.read().split()
	i = 0

	for word in file_data:

		#check if the word is found
		if sorted(word) == sorted(search_word):
			print("Original Word Found: ", word)
			# return

		#check if the reverse word is found
		# if word == search_word[::-1]:
		# 	print("Reverse Word Found: ", search_word[::-1])

		search_substring(search_word=search_word, word=word)

		i += 1

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

	#download the data and save it in a text file
	download_data()


	#read word input from the cli
	parser = argparse.ArgumentParser()
	# parser.add_argument('word')
	# parser.add_argument('filename', )
	parser.add_argument('-f', '--filename', help='Word Filename',required=False)
	parser.add_argument('-w', '--word', help='Word', required=True)
	args = parser.parse_args()


	print("======================================")
	print("Word List filename: ", args.filename)
	print("Word to search for: ", args.word)
	print("======================================")

	search_word(args.word)
	

