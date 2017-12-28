#! /usr/bin/env python
# Day 9 - Stream Processing

import sys
sys.path.append("../../..")

from python_util import prints, get_input

def main():
	print "*** Part 1 ***"
	prints(r"{}", score, 1)
	prints(r"{{{}}}", score, 6)
	prints(r"{{},{}}", score, 5)
	prints(r"{{{},{},{{}}}}", score, 16)
	prints(r"{<a>,<a>,<a>,<a>}", score, 1)
	prints(r"{{<ab>},{<ab>},{<ab>},{<ab>}}", score, 9)
	prints(r"{{<!!>},{<!!>},{<!!>},{<!!>}}", score, 9)
	prints(r"{{<a!>},{<a!>},{<a!>},{<ab>}}", score, 3)
	prints(get_input()[0], score)

	print "*** Part 2 ***"
	prints(r"<>", garbage, 0)
	prints(r"<random characters>", garbage, 17)
	prints(r"<<<<>", garbage, 3)
	prints(r"<{!>}>", garbage, 2)
	prints(r"<!!>", garbage, 0)
	prints(r"<!!!>>", garbage, 0)
	prints(r'<{o"i!a,<{i<a>', garbage, 10)
	prints(get_input()[0], garbage)

def score(stream):
	return process(stream)[0]

def garbage(stream):
	return process(stream)[1]

def process(stream):
	score = 0
	level = 0
	garbage_count = 0
	escaped = False
	garbage = False
	for c in stream:
		if garbage:
			if escaped:
				escaped = False
			elif c == '!':
				escaped = True
			elif c == '>':
				garbage = False
			else:
				garbage_count += 1
		elif c == '<':
			garbage = True
		elif c == '{':
			level += 1
		elif c == '}':
			score += level
			level -= 1
	return score, garbage_count

if __name__ == '__main__':
	main()
