#! /usr/bin/env python
# Day 5 - Doesn't He Have Intern-Elves For This?

import re

vvv = re.compile(r'.*([aeiou].*[aeiou].*[aeiou]).*')
def triple_vowel(text):
	return bool(vvv.search(text))

ll = re.compile(r'.*(\w)(?=\1).*')
def doubled_letter(text):
	return bool(ll.search(text))

wl = re.compile(r'.*(ab|cd|pq|xy).*')
def whitelist(text):
	return not bool(wl.search(text))

def is_nice(text):
	return triple_vowel(text) and doubled_letter(text) and whitelist(text)

dlt = re.compile(r'.*(\w\w).*(?=\1).*')
def doubled_letter_twice(text):
	return bool(dlt.search(text))

dw = re.compile(r'.*(\w)\w(?=\1).*')
def doubled_split(text):
	return bool(dw.search(text))

def is_nice_v2(text):
	return doubled_letter_twice(text) and doubled_split(text)

def main():
	unknown_lines = get_input()

	nice_strings = 0
	for s in unknown_lines:
		nice_strings += 1 if is_nice(s) else 0
	print('Of {} lines, {} are nice'.format(len(unknown_lines), nice_strings))

	nice_strings = 0
	for s in unknown_lines:
		nice_strings += 1 if is_nice_v2(s) else 0
	print('Of {} lines, {} are nice under new criteria'.format(len(unknown_lines), nice_strings))

def get_input():
	with open('../day_5_input.txt') as directions:
		return [d.strip() for d in directions]

if __name__ == "__main__":
	main()
