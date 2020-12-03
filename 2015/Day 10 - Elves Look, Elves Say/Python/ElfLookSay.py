#! /usr/bin/env python
# Day 10 - Elves Look, Elves Say

import re, itertools

gs = re.compile(r'((\d)(?:\2*))')
def gen_seq(inpt):
	while True:
		inpt = ''.join(str(len(seq)) + ch for seq, ch in gs.findall(inpt))
		yield inpt

def main():
	for index, result in enumerate(itertools.islice(gen_seq('3113322113'), 50)):
		if index == 39:
			print(len(result))
		elif index == 49:
			print(len(result))

if __name__ == "__main__":
	main()
