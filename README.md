# jumble_solver

Build a jumble solver in Python3

## Implementation

The program takes in a word from the user and searches for all the matches to this word in a huge list of words. This includes Anagrams as well as sub-string matches of the original search word. This is quite similar to the string matching problem (also known as *"the needle in a haystack"*). This algorithm finds its application in multiple domains including Pattern Recognition, Document Search, and many more.  

**What are Anagrams?**

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word *anagram* itself can be rearranged into *nagaram*, also the word binary into brainy and the word *adobe *into *abode*. 

The program searches for words in the list (text file) which are anagrams to the search word provided by the user. For this, the both the search word and the word from the list are *sorted*. Sorting a string in python arranges all the letters in the word in alphabetical order. Next, it would compare both the strings to check if the letters match. If all the letters match, they are anagrams and hence a match!

The program also searches for sub-strings of the original word in the list. Sub-string search can be done in various ways. The classic way would be use the naive method. In this method, the substring (the word to be searched) is matched to the string (the word from the list) letter by letter. When we have a letter mismatch, we move to the next letter. This is an inefficient method to perform the search. The time complexity of this method is `O(mn)` where `m` is the length of the substring, `n` is the length of the string. KMP algorithm skips matching the part which has been already matched. This way, we do not need to move one step at a time, but skip the part that alredy has been matched. This will reduce the complexity less than O(mn) as now it will not be iterating over all the letter of the string (length `n`). This can be achieved by creating an aux string. The aux string will store the index value till what we can skip matching. 


## Dependencies

  * Enivronment: Linux
  
  * Python 3.x ([Download](https://www.python.org/downloads/))
  
  * requests

  * argparse

    pip3 install --user -r requirements.txt

   

## Dataset 

The following implementation requires a list of English words. The program uses a `.txt`. This file can either be provided by the user or the program can download one byitself. 

### Download through code: 

The dataset used in the code is [here](http://www.mit.edu/~ecprice/wordlist.10000). The code will download the dataset and save it in a `word_list.txt` file. The location of this file is `./../Data/word_list`. If this file exists, it will skip the download step. 

### Manual Download and Save:

You can manually download any dataset or used an existing dataset. The file needs to be a `.txt` file and would conatin all the words either separated by space or one word on each line. You can refer to the sample from the above section. A sample file is also available in the `/Data` folder. 

## How to run   

The repository can be cloned on a local machine using the command

    git clone https://github.com/revati-naik/jumble_solver

The program file `jumble_solver.py` can be run to execute the program. The program takes in few inputs from the command line. 

1. `[-f path/to/file/] [OPTIONAL]` : This is the path to the `.txt` file provided by the user. Default action would be that the dataset will be automatically downloaded from the link in the code and save as `/Data/word_list.txt` and this dataset (list of words) will be used for search (match). 

2. `[-w search_word] [REQUIRED]` : This is the word for which the program needs to find match for in the text file. 



   ` python3 jumble_solver.py -w search_word [-f path/to/file/]`



**To run the program and use the default dataset**

The dataset will be downloaded from the link (through code) and saved in the `/Data` directory as `word_list.txt`. 

    python3 jumble_solver.py -w search_word [REQUIRED]

eg. 

    python3 jumble_solver.py -w listen

**To run the program and use a text file by the user**

    python3 jumble_solver.py -f path/to/file [REQUIRED] -w search_word [REQUIRED]

