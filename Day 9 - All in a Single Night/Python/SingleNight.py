#! /usr/bin/env python
# Day 9 - All in a Single Night

import itertools, re

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

def calc_distance(lookup, path):
	return sum(lookup[p][s] for p, s in pairwise(path))

pd = re.compile(r'(\w+) to (\w+) = (\d+)')
def main():
	locations = get_input()

	distance_lookup = {}
	for l in locations:
		m = pd.match(l)
		if m:
			city_1 = m.group(1)
			city_2 = m.group(2)
			distance = m.group(3)

			if city_1 not in distance_lookup:
				distance_lookup[city_1] = {}
			distance_lookup[city_1][city_2] = int(distance)

			if city_2 not in distance_lookup:
				distance_lookup[city_2] = {}
			distance_lookup[city_2][city_1] = int(distance)
		else:
			raise ValueError("Could not parse '{}'".format(l))

	print min(calc_distance(distance_lookup, path) for path in itertools.permutations(distance_lookup.keys()))

def get_input():
	with open('../day_9_input.txt') as directions:
		return [d.strip() for d in directions]

if __name__ == "__main__":
	main()
