#! /usr/bin/env python
# Day 3 - Spiral Memory

import sys
sys.path.append("../../..")

from python_util import prints, get_input
from itertools import permutations

def main():
	print("*** Part 1 ***")

	prints(1, spiral_dist, 0)
	prints(3, spiral_dist, 2)
	prints(7, spiral_dist, 2)
	prints(12, spiral_dist, 3)
	prints(15, spiral_dist, 2)
	prints(20, spiral_dist, 3)
	prints(23, spiral_dist, 2)
	prints(1024, spiral_dist, 31)
	for target in get_input():
		prints(int(target), spiral_dist)

def spiral_dist(pos):
	return sum(abs(c) for c in spiral_coords(pos))

def spiral_coords(pos):
	ring = 0
	while (2*ring + 1) ** 2 < pos:
		ring += 1

	offset = pos - (2*(ring-1) + 1) ** 2
	side = 2*ring

	if offset < side:
		return ring, side - offset - ring
	elif offset < 2 * side:
		return 2 * side - offset - ring, ring
	elif offset < 3 * side:
		return -ring, 3 * side - offset - ring
	else:
		return 4 * side - offset - ring, ring

if __name__ == '__main__':
	main()
