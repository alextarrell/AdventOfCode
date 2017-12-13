#! /usr/bin/env python
# Day 6 - Memory Reallocation

import sys
sys.path.append("../../..")

from python_util import prints, get_input

def main():
	print "*** Part 1 ***"

	prints('0 2 7 0', reallocate, 5)
	for banks in get_input():
		prints(banks.replace('\t', ' '), reallocate)

def reallocate(banks):
	banks = [int(b) for b in banks.split(' ')]

	uniqs = set()
	while tuple(banks) not in uniqs:
		uniqs.add(tuple(banks))
		idx = banks.index(max(banks))
		bucket = banks[idx]
		banks[idx] = 0
		while bucket:
			idx = idx + 1 if idx < len(banks) - 1 else 0
			banks[idx] += 1
			bucket -= 1

	return len(uniqs)

if __name__ == '__main__':
	main()
