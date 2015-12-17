#! /usr/bin/env python
# Day 14 - Reindeer Olympics

import re
from collections import namedtuple

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
	return moving_time * reindeer.speed

rp = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.')
def main():
	stats = get_input()
	reindeer = [Reindeer(*map(try_int, rp.match(s).groups())) for s in stats]

	print max(calc_travel(2503, r) for r in reindeer)

def get_input():
	with open('../day_14_input.txt') as stats:
		return [s.strip() for s in stats]

if __name__ == "__main__":
	main()
