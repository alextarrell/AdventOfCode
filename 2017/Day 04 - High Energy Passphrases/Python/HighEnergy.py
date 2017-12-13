#! /usr/bin/env python
# Day 4 - High-Energy Passphrases

import sys
sys.path.append("../../..")

from python_util import prints, get_input
from collections import Counter
from itertools import permutations

def main():
	print "*** Part 1 ***"

	prints("aa bb cc dd ee", no_dupes, True)
	prints("aa bb cc dd aa", no_dupes, False)
	prints("aa bb cc dd aaa", no_dupes, True)
	prints(get_input(), count_no_dupes)

	prints("abcde fghij", no_anadupes, True)
	prints("abcde xyz ecdab", no_anadupes, False)
	prints("a ab abc abd abf abj", no_anadupes, True)
	prints("iiii oiii ooii oooi oooo", no_anadupes, True)
	prints("oiii ioii iioi iiio", no_anadupes, False)
	prints(get_input(), count_no_anadupes)

def no_dupes(phrase):
	return Counter(phrase.split(' ')).most_common(1)[0][1] == 1

def count_no_dupes(phrases):
	return len(filter(None, [no_dupes(p) for p in phrases]))

def no_anadupes(phrase):
	anagrams = set()
	for part in phrase.split(' '):
		p_grams = set("".join(p) for p in permutations(part))
		if p_grams & anagrams:
			return False
		anagrams |= p_grams
	return True

def count_no_anadupes(phrases): 
	return len(filter(None, [no_anadupes(p) for p in phrases]))

if __name__ == '__main__':
	main()
