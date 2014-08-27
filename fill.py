'''
Author:		Ryan Wagner
		rkwagner@ucsd.edu
		https://github.com/rkwagner
Date:		August 26, 2014
Description:	Writes convincing filler text.
		Constraints:
		Input - Number of words
		Sentences, 	2-8 words long.
		Words, 		1-12 chars long.
		Sentences,	Start with a cap, end with period.
		Linebreak,	15% chance.
		Paragraph,	50% of linebreak.
'''

import random

def letters():
	a = random.uniform( 1 , 100 )
	if a < 8.167:
		return 'a'
	elif a < 9.659:
		return 'b'
	elif a < 12.441:
		return 'c'
	elif a < 16.694:
		return 'd'
	elif a < 29.396:
		return 'e'
	elif a < 31.676:
		return 'f'
	elif a < 33.691:
		return 'g'
	elif a < 39.785:
		return 'h'
	elif a < 46.751:
		return 'i'
	elif a < 46.904:
		return 'j'
	elif a < 47.676:
		return 'k'
	elif a < 51.701:
		return 'l'
	elif a < 54.107:
		return 'm'
	elif a < 60.856:
		return 'n'
	elif a < 68.363:
		return 'o'
	elif a < 70.292:
		return 'p'
	elif a < 70.387:
		return 'q'
	elif a < 76.374:
		return 'r'
	elif a < 82.701:
		return 's'
	elif a < 91.757:
		return 't'
	elif a < 94.515:
		return 'u'
	elif a < 95.493:
		return 'v'
	elif a < 97.853:
		return 'w'
	elif a < 98.003:
		return 'x'
	elif a < 99.977:
		return 'y'
	return 'z'

def word():
	word_len = random.randint( 1 , 12 )
	return word_len

def sentence():
	sent_len = random.randint( 2 , 8 )
	return sent_len

def linebreak():
	line_break = random.randint( 1 , 100 )
	return 2 if line_break > 93 else 1 if line_break > 85 else 0

#main function.
'''
Step 1: Get user input word count.
Step 2: Use that as a definition of max words (max loops?)
Step 3: Iterate using the three above functions for word_length, 
	sentence_length, and chance of line/paragraph break.

	-If word length > 12, use an integer instead of looping through
	the word.
	-When a sentence starts, the first letter of the first word is 
	capitalized.
	-When it ends, insert a period.
'''

