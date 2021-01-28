

# MIT License

# Copyright (c) 2021 Revati Naik

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# @mainpage Jumble Solver Project
# @file    jumble_solver.py
# @author  Revati Naik
# @version 1.0
# @brief JUmble Solver (word match) implementation
#
# @section DESCRIPTION
#
#  python implementation for jumble solver which searches all the matches for the word
#  (string) and the sub string in a list of english words
# @section libraries_main Libraries/Modules
# - argparse
# - requests
# @section jumble_solver Author(s)
# - Created by Revati Naik on 01/28/2021.
# Copyright (c) 2021 Revati Naik


# Imports
from __future__ import print_function

import sys
import os.path
import argparse
import requests


# Functions
def download():
    """
    !Downloads the word list as dataset
    """
    # link to the words list dataset
    link = "http://www.mit.edu/~ecprice/wordlist.10000"

    # try to connect to the specified url. Throw an exception on failure
    try:

        # mopen the link and read the data on the link
        response = requests.get(link)
        words_data = response.text

    # failed to connect to the url
    except requests.exceptions.ConnectionError as e:
        print("Problem connecting to the url! Try Again")
        sys.exit()

    try:
        # file path to data set (.txt) file
        data_file_path = "./../Data/word_list.txt"

        # checks if the data set file exists
        # if not true, will create a new file
        if not os.path.isfile(data_file_path):
            print("Downloading Dataset")

            # opening the file
            file = open("./../Data/word_list.txt", "w+")

            # writing the downloaded data to the file
            file.write(words_data)
            print("Dataset Downloaded Successfully")

        # if data file already exists
        else:
            print("Data already exists.All set!")

    # Data folder does not exist
    except FileNotFoundError as e:
        print("Could not open the folder (/Data) to \
            save the word list document")
        sys.exit()


def search_word(search_word, file_path='word_list.txt'):
    """
    !Searchs for the word in the word list

    @param      search_word:  The user deifned word for which we find the match
    @type       search_word:  { string }
    @param      file_path:    The filename which contains a
                              list of english words
    @type       file_path:    { string}
    """

    # try to open the file. Throws an exception if file does not exist

    if file_path == 'word_list.txt':
        dir_path = './../Data/word_list.txt'
    else:
        dir_path = file_path

    try:
        # open the word list file and read it
        file = open(dir_path, "r")
        file_data = file.read().split()

    except FileNotFoundError as e:
        print("File does not exist!")
        sys.exit()

    # iterating over every word in the file
    for word in file_data:

        # check if the search word matches the word word in the file
        # checks for anagrams
        if sorted(word) == sorted(search_word):

            # print the word from the list
            print(word)

        # tries to search for substring matches
        search_substring(search_word=search_word, word=word)


def create_aux(word):
    """
    !Creates an auxiliary array

    @param      word:  The word from the word list
    @type       word:  { string }

    @returns:   { Auxiliary array }
    @rtype:     { list }
    """

    # initializing the aux array of lenth equal to the substring length
    aux = [0] * len(word)

    # at index 0, there is no duplicate letter, hence that would always be 0,
    # so we start from index 1
    i = 1

    # index of the first mismatch
    j = 0
    while i < len(word):

        # when there is a match, prefix = sufix[j-1]
        if word[i] == word[j]:
            j += 1
            aux[i] = j
            i += 1
        # when there is a mismatch, we check index of previous possible prefix
        elif word[i] != word[j] and j != 0:
            j = aux[j-1]
        # when no prefix is found which is euqal to suffix for index i
        else:
            aux[i] = 0
            i += 1

    return aux


def search_substring(search_word, word):
    """
    !Searches for the substring match in the word list

    @param      search_word:  The user deifned word for which we find the match
    @type       search_word:  { string }
    @param      word:         The word from the word list
    @type       word:         { string }
    """

    # creates the aux array for the word
    aux = create_aux(word)

    # counter for word from the word list (substring)
    i = 0

    # counter for search word (string)
    j = 0

    while j < len(search_word):

        # mismatch condition
        if word[i] != search_word[j]:

            if i == 0:
                # start next matching from the immediate next
                # letter in the word string
                j += 1
            else:
                # start comparing from aux[i-1], as word[0,..,aux[i-1]-1]
                # already matches
                i = aux[i-1]
        else:
            i += 1
            j += 1

            # match pattern found
            if i == len(word):

                # prints the match word found from the word list
                print(word)

                # continues to find more matches in the word
                i = aux[i-1]


if __name__ == '__main__':
	""" 
	!Main Program
	"""

    parser = argparse.ArgumentParser()

    # read the filename from the user. This is an optional argument
    # deafult is the already available dataset in ./Data folder
    parser.add_argument('-f', '--filename', help='Word List Filename',
                        required=False, default='word_list.txt')

    # read the user defined word from the cli
    parser.add_argument('-w', '--word', help='Search Word', required=True)

    args = parser.parse_args()

    # user selects to download the dataset
    if args.filename == 'word_list.txt':
        download()

    print("======================================")
    print("Word List filename: ", args.filename)
    print("Word to search for: ", args.word)
    print("======================================")

    # download the data and save it in a text file
    search_word(search_word=args.word, file_path=args.filename)
