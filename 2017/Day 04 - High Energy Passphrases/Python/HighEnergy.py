#! /usr/bin/env python
# Day 4 - High-Energy Passphrases

import sys
sys.path.append("../../..")

from python_util import prints, get_input
from collections import Counter

def main():
	print "*** Part 1 ***"

	prints("aa bb cc dd ee", no_dupes, True)
	prints("aa bb cc dd aa", no_dupes, False)
	prints("aa bb cc dd aaa", no_dupes, True)
	prints(get_input(), count_no_dupes)

def no_dupes(phrase):
	return Counter(phrase.split(' ')).most_common(1)[0][1] == 1

def count_no_dupes(phrases):
	return len(filter(None, [no_dupes(p) for p in phrases]))

if __name__ == '__main__':
	main()
