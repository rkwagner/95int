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

def word():
	word_len = random.randint( 1 , 12 )
	return word_len

def sentence():
	sent_len = random.randint( 2 , 8 )
	return sent_len

print word()

