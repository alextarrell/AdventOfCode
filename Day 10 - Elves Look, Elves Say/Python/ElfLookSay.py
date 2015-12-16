#! /usr/bin/env python
# Day 10 - Elves Look, Elves Say

import re, itertools

gs = re.compile(r'((\d)(?:\2*))')
def gen_seq(inpt):
	while True:
		inpt = ''.join(str(len(seq)) + ch for seq, ch in gs.findall(inpt))
		yield inpt

def main():
	print len(list(itertools.islice(gen_seq('3113322113'), 40))[-1])

if __name__ == "__main__":
	main()
