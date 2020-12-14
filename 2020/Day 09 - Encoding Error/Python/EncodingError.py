# Day 9 - Encoding Error
import sys
from itertools import combinations

def find_weakness(data, length):
	for idx, val in enumerate(data[length:]):
		if all(sum(pair) != val for pair in combinations(data[idx:idx + length], 2)):
			return val

def main():
	data = [int(line.strip()) for line in sys.stdin.readlines()]

	preamble_size = 25
	if len(data) < 25:
		# Note that the test data has a preamble of 5 while the input is 25 so if our
		# data set is short we just assumes it's test data Assumes it's test data
		preamble_size = 5

	print(find_weakness(data, preamble_size))

if __name__ == '__main__':
	main()
