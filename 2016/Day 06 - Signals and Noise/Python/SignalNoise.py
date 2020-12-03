#! /usr/bin/env python
# Day 6 - Signals and Noise

from collections import Counter

def main():
	signals = get_input()

	corrected = ''.join([Counter(s).most_common(1)[0][0] for s in zip(*signals)])
	print('The error-corrected message is {}'.format(corrected))

	corrected = ''.join([Counter(s).most_common()[-1][0] for s in zip(*signals)])
	print('The real error-corrected message is {}'.format(corrected))

def get_input():
	with open('../day_6_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
