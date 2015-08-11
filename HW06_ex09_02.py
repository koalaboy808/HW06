#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
def has_no_e(word):
	if "e" not in word:
		return True
	False

def count_no_e():
	with open("words.txt") as in_fin:
		with_e = 0
		without_e = 0
		for line in in_fin:
			if has_no_e(line):
				without_e += 1
			else:
				with_e += 1

	# get decimal then convert to percentage
	decimal = (float(without_e) / (float(with_e) + float(without_e)))
	percentage = round(decimal*100,1)
	print(str(percentage) + "%")


##############################################################################
def main():

    count_no_e()

if __name__ == '__main__':
    main()
