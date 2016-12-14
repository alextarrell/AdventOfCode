#! /usr/bin/env python
# Day 5 - How About a Nice Game of Chess?

from hashlib import md5
from itertools import islice, count

def gen_hash(base, i):
	return md5(base + str(i)).hexdigest()

def main():
	doors = get_input()

	for door in doors:
		hashs = list(islice((gen_hash(door, i) for i in count() if gen_hash(door, i)[:5] == '00000'), 8))
		print 'The password for door ID {} is {}'.format(door, ''.join(h[5] for h in hashs))

def get_input():
	with open('../day_5_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
