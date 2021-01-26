import urllib
import os.path
from urllib.request import urlopen




##
## Downloads the word list as data set
##
def download_data():

	# link to the words list dataset
	# link = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
	link = "http://www.mit.edu/~ecprice/wordlist.10000"
	data = urlopen(link)
	words_data = data.read().decode('utf-8')

	# file path to data set (.txt) file
	data_file_path = "./../Data/word_list.txt"

	## Checks if the data set file exists. If not true, will create a new file
	if not os.path.isfile(data_file_path):
		file = open("./../Data/word_list.txt","w+")
		file.write(words_data)

	else:
		print("Data already exists.All set!")






if __name__ == '__main__':

	download_data()

	file = open("./../Data/word_list.txt","r")
	file_data = file.read()
	print(file_data[0])
