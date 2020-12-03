#! /usr/bin/env python
# Day 2 - Corruption Checksum

import sys
sys.path.append("../../..")

from python_util import prints, get_input
from itertools import permutations

def main():
	print("*** Part 1 ***")

	sample = [
		"5 1 9 5",
		"7 5 3",
		"2 4 6 8"
	]

	prints(sample, checksum, 18)
	prints(get_input(), checksum)

	print("*** Part 2 ***")
	sample = [
		"5 9 2 8",
		"9 4 7 3",
		"3 8 6 5"
	]

	prints (sample, checksum2, 9)
	prints(get_input(), checksum2)


def checksum(sheet):
	sheet = [[int(v) for v in row.replace('\t', ' ').split(' ')] for row in sheet]
	return sum(max(row) - min(row) for row in sheet)

def checksum2(sheet):
	sheet = [[int(v) for v in row.replace('\t', ' ').split(' ')] for row in sheet]
	return sum(next(abs(v1 / v2) for v1, v2 in permutations(row, 2) if v1 % v2 == 0) for row in sheet)

if __name__ == '__main__':
	main()
