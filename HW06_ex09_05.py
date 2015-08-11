#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body
def uses_all(word, string):
	# will use this variable to test if all characters are verified
	test = 0

	# start for loop on each character in the given string
	for character in string:
	# if the character is in word then increment test by 1
		if character in word:
			test += 1

	# if the length of string equals final test number then return True
	if test == len(string):
		return True
	else:
		return False

def number_uses_all(string):

	# test will eventually provide number of times letters in string are used
	test = 0 

	# read each line in txt file and call uses_all to count number of times
	with open("words.txt") as f_in:
		for line in f_in:
			if uses_all(line, string):
				test += 1
	print(test)

##############################################################################
def main():

    number_uses_all("aeiou")
    number_uses_all("aeiouy")

if __name__ == '__main__':
    main()
