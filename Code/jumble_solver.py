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
		if word == search_word:
			print("Original Word Found at ", i)
			# return

		#check if the reverse word is found
		if word == search_word[::-1]:
			print("Reverse Word Found: ", search_word[::-1])

		i += 1

if __name__ == '__main__':

	#download the data and save it in a text file
	download_data()
	

	#read word input from the cli
	parser = argparse.ArgumentParser()
	parser.add_argument('word')
	args = parser.parse_args()
	print("Word to search for: ", args.word)

	search_word(args.word)
	
