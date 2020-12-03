#! /usr/bin/env python
# Day 14 - Reindeer Olympics

import re
from collections import defaultdict, namedtuple
from operator import itemgetter

Reindeer = namedtuple('Reindeer', 'name, speed, move_time, rest_time')

def try_int(inpt):
	try:
		return int(inpt)
	except ValueError:
		return inpt

def calc_travel(time, reindeer):
	interval = reindeer.move_time + reindeer.rest_time
	sets = time // interval
	remainder = time % interval
	moving_time = reindeer.move_time * sets
	moving_time += reindeer.move_time if remainder > reindeer.move_time else remainder
	return moving_time * reindeer.speed, reindeer.name

rp = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.')
def main():
	stats = get_input()
	reindeer = [Reindeer(*list(map(try_int, rp.match(s).groups()))) for s in stats]

	m = max((calc_travel(2503, r) for r in reindeer), key=itemgetter(0))
	print('{} went {} km'.format(m[1], m[0]))

	reindeer_points = defaultdict(list)
	for t in range(1, 2503):
		results = [calc_travel(t, r) for r in reindeer]
		m = max(results, key=itemgetter(0))[0]

		for r in results:
			if r[0] == m:
				reindeer_points[r[1]].append(r[0])

	scores = [(r[0], len(r[1])) for r in reindeer_points.items()]
	m = max(scores, key=itemgetter(1))
	print('{} had {} pts'.format(m[0], m[1]))

def get_input():
	with open('../day_14_input.txt') as stats:
		return [s.strip() for s in stats]

if __name__ == "__main__":
	main()
