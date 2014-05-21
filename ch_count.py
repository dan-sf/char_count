#!/usr/bin/python

#--------------------------------------------
# Char count script: Maintained by Dan Fowler
# Website: dsfcode.com
# Version 1.0.0
#--------------------------------------------

import sys
import argparse

# Parse the args
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--char", action="store", help="The character that will be counted on each line of input", dest="char")
args = vars(parser.parse_args())

# Loop through stdin and count the number of input chars on each row
for row in sys.stdin:
	count = 0
	for ch in row:
		if ch == args['char']:
			count += 1
	print count

