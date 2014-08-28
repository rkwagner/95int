'''
Author:		Ryan Wagner
		rkwagner@ucsd.edu
		https://github.com/rkwagner
Date:		August 26, 2014
Description:	Writes convincing filler text.
'''

from __future__ import print_function
import random

def letters( ):
	a = random.uniform( 0 , 100 )
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

def word( ):
	word_len = random.randint( 1 , 13 )
	return word_len

def sentence( ):
	sent_len = random.randint( 3 , 9 )
	return sent_len

def linebreak( ):
	line_break = random.randint( 1 , 100 )
	return 2 if line_break > 93 else 1 if line_break > 85 else 0

#main function.
try:
	word_count = int( input(  "Filler Length: " ) )
except (SyntaxError, NameError):
	print( 'Not a valid integer.' )
else:
	a = 0
	while a < word_count:
		sent_len = sentence( )
		a += sent_len
		for b in range( 0 , sent_len ):
			word_len = word( )
			if word_len == 13:
				print( random.randint( 0 , 10000 ), end = '' ),
			else:
				for c in range( 0 , word_len ):
					if b == 0 and c == 0:
						print( letters( ).capitalize( ),
								end = '' ),
					else:
						print ( letters( ), end = '' ),
			if b < sent_len - 1:
				print( ' ', end = '' ),
			else:
				print( '. ', end = '' ),
		break_type = linebreak()
		if break_type == 2:
			print( '\n' )
		elif break_type == 1:
			print( '' )
	print( '' )
