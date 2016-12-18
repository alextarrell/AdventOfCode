#! /usr/bin/env python
# Day 9 - Explosives in Cyberspace

import re

r_marker = re.compile(r'\((\d+)x(\d+)\)')

def decom(f, recurse=True):
	file_length = 0
	start = 0
	while start < len(f):
		marker = r_marker.search(f, start)
		if not marker:
			file_length += len(f[start:])
			break

		length = int(marker.group(1))
		repeat = int(marker.group(2))

		file_length += len(f[start:marker.start()])
		if recurse:
			file_length += decom(f[marker.end():marker.end() + length]) * repeat
		else:
			file_length += len(f[marker.end():marker.end() + length]) * repeat

		start = marker.end() + length

	return file_length

def main():
	files = get_input()

	for idx, f in enumerate(files):
		print 'The decompressed length of file {} is {}, or {} with recursion'.format(idx + 1, decom(f, False), decom(f))

def get_input():
	with open('../day_9_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
