#! /usr/bin/env python
# Day 1 - No Time for a Taxicab

NORTH = 0
EAST  = 1
SOUTH = 2
WEST = 3

def main():
	maps = get_input()
	for directions in maps:
		orient = NORTH
		x, y = 0, 0

		for d in directions.split(', '):
			if d[0] == 'R':
				orient += 1
			elif d[0] == 'L':
				orient -= 1
			else:
				print "Invalid direction: '" + d + "'"
				continue

			if orient < NORTH:
				orient = WEST
			elif orient > WEST:
				orient = NORTH

			try:
				dist = int(d[1:])
			except:
				print "Invalid direction: '" + d + "'"
				continue

			if orient == NORTH:
				y += dist
			elif orient == SOUTH:
				y -= dist
			elif orient == EAST:
				x += dist
			elif orient == WEST:
				x -= dist

		print 'Final position of ({}, {}) is {} blocks away'.format(x, y, abs(x) + abs(y))


def get_input():
	with open('../day_1_input.txt') as stats:
		return [s.strip() for s in stats]


if __name__ == "__main__":
	main()
