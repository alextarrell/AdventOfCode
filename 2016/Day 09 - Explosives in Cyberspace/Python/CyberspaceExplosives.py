#! /usr/bin/env python
# Day 9 - Explosives in Cyberspace

import re

r_marker = re.compile(r'\((\d+)x(\d+)\)')

def main():
	files = get_input()

	for idx, f in enumerate(files):
		out = ""
		start = 0
		while start < len(f):
			marker = r_marker.search(f, start)
			if not marker:
				out += f[start:]
				break

			length = int(marker.group(1))
			repeat = int(marker.group(2))

			out += f[start:marker.start()] + f[marker.end():marker.end() + length] * repeat
			start = marker.end() + length

		print 'The decompressed length of file {} is {}'.format(idx + 1, len(out))

def get_input():
	with open('../day_9_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
