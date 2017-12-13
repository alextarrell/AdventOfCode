#! /usr/bin/env python
# Day 5 - A Maze of Twisty Trampolines, All Alike

import sys
sys.path.append("../../..")

from python_util import prints, get_input

def main():
	print "*** Part 1 ***"

	prints(['0', '3', '0', '1', '-3'], follow, 5)
	prints(get_input(), follow)

def follow(instructions):
	instructions = [int(j) for j in instructions]
	jumps = 0
	idx = 0
	while idx < len(instructions):
		instructions[idx] += 1
		idx += instructions[idx] - 1
		jumps += 1
	
	return jumps

if __name__ == '__main__':
	main()
