#! /usr/bin/env python
# Day 4 - The Ideal Stocking Stuffer

from hashlib import md5

def find_hash(key, ipt):
	return str(md5(key + str(ipt)).hexdigest())

def main():
	i = 0
	while not find_hash('yzbqklnj', i).startswith('00000'):
		i += 1
	print i

if __name__ == "__main__":
	main()
