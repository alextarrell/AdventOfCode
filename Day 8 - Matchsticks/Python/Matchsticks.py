#! /usr/bin/env python
# Day 8 - Matchsticks

import re

def len_code(line):
	return len(line)

lt = re.compile(r'\\x[0-f]{2}|\\[\\"]|.')
def len_true(line):
	return len(lt.findall(line[1:-1]))

def main():
	lines = get_input()
	total_diff = 0
	for l in lines:
		total_diff += len_code(l) - len_true(l)
	print total_diff

def get_input():
	with open('../day_8_input.txt') as directions:
		return [d.strip() for d in directions]

if __name__ == "__main__":
	main()
