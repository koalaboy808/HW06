#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body
def avoids(word, forbidden):
	if forbidden not in word:
		return True
	False

def avoids_total():
	forbidden = raw_input("Input a forbidden string-- ")
	is_forbidden = 0

	with open("words.txt") as fin:
		for line in fin:
			if avoids(line, forbidden):
				is_forbidden += 1
	print(is_forbidden)

# not sure how to do number three yet... is this some permutation thing??



##############################################################################
def main():
    avoids_total()

if __name__ == '__main__':
    main()
