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
		stops = set((0, 0))
		dupes = []

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

			for _ in xrange(dist):
				if orient == NORTH:
					y += 1
				elif orient == SOUTH:
					y -= 1
				elif orient == EAST:
					x += 1
				elif orient == WEST:
					x -= 1

				if (x, y) not in stops:
					stops.add((x, y))
				else:
					dupes.append((x, y))

		print 'You\'ve arrived at ({}, {}), {} blocks from the start.'.format(x, y, abs(x) + abs(y)),
		if dupes:
			print '({}, {}) at {} blocks was the first location visited twice'.format(dupes[0][0], dupes[0][1], abs(dupes[0][0]) + abs(dupes[0][1]))
		else:
			print 'No locations were visited twice'


def get_input():
	with open('../day_1_input.txt') as stats:
		return [s.strip() for s in stats]


if __name__ == "__main__":
	main()
