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

	##Checks if the data set file exists. If not true, will create a new file
	if not os.path.isfile(data_file_path):
		file = open("./../Data/word_list.txt", "w+")
		file.write(words_data)

	else:
		print("Data already exists.All set!")

def search_word(search_word):

	#open the word list file and read it
	file = open("./../Data/word_list.txt", "r")
	file_data = file.read().split()
	i = 0

	for word in file_data:
		if word == search_word:
			print("Word Found! at ", i)
			return
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
	
