#! /usr/bin/env python
# Day 13 - Knights of the Dinner Table

import re, itertools

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

def optimal(guests):
	optimal_combination = None
	optimal_happiness = 0
	for g in itertools.permutations(guests.keys()):
		g = list(g)
		g.append(g[0])

		happiness = 0
		for p1, p2 in pairwise(iter(g)):
			happiness += guests[p1][p2] + guests[p2][p1]

		if happiness > optimal_happiness:
			optimal_combination = g[:-1]
			optimal_happiness = happiness

	return optimal_happiness, optimal_combination

glp = re.compile(r'(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*)\.')
def main():
	guest_list = get_input()

	guests = {}
	for g in guest_list:
		m = glp.match(g)
		if m:
			p1 = m.group(1)
			gainlose = 1 if m.group(2) == 'gain' else -1
			amt = int(m.group(3))
			p2 = m.group(4)

			if p1 not in guests:
				guests[p1] = {}

			guests[p1][p2] = amt * gainlose
		else:
			raise ValueError('Could not match input: {}'.format(g))

	print optimal(guests)

	for g in guests.itervalues():
		g['Me'] = 0
	guests['Me'] = {g: 0 for g in guests.keys()}

	print optimal(guests)

def get_input():
	with open('../day_13_input.txt') as directions:
		return [d.strip() for d in directions]

if __name__ == "__main__":
	main()
