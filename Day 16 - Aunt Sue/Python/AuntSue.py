#! /usr/bin/env python
# Day 16 - Aunt Sue

import re

ps = re.compile(r'(\w+): (\d+)')

master_sue = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1
}
def score(sue):
	return (sum(1 if str(master_sue[m.group(1)]) == m.group(2) else 0
				  for m in ps.finditer(sue)), sue)

def main():
	sues = get_input()

	scores = [score(s) for s in sues]
	print max(scores)

def get_input():
	with open('../day_16_input.txt') as sues:
		return [s.strip() for s in sues]

if __name__ == "__main__":
	main()
