#! /usr/bin/env python
# Day 7 - Recursive Circus

import sys
sys.path.append("../../..")

from python_util import prints, get_input
import re

re_struct = re.compile(r"(\w+) \((\d+)\)(?: -> (.*))?")

class Tower():
	def __init__(self, structure):
		match = re_struct.match(structure)
		self.name = match.group(1)
		self.weight = int(match.group(2))
		self.subs = filter(None, (match.group(3) or "").split(', '))
		self.parent = None

	def link(self, lookup):
		self.subs = [lookup[sub] for sub in self.subs]
		for tower in self.subs:
			tower.parent = self

	def __str__(self):
		if self.subs:
			return "{} ({}) -> [{}]".format(self.name, self.weight, ', '.join(str(s) for s in self.subs))
		else:
			return "{} ({})".format(self.name, self.weight)
	__repr__ = __str__

def main():
	print "*** Part 1 ***"

	sample = [
		"pbga (66)",
		"xhth (57)",
		"ebii (61)",
		"havc (66)",
		"ktlj (57)",
		"fwft (72) -> ktlj, cntj, xhth",
		"qoyq (66)",
		"padx (45) -> pbga, havc, qoyq",
		"tknk (41) -> ugml, padx, fwft",
		"jptl (61)",
		"ugml (68) -> gyxo, ebii, jptl",
		"gyxo (61)",
		"cntj (57)"
	]

	prints(sample, find_bottom, 'tknk')
	prints(get_input(), find_bottom)

def construct(structures):
	towers = [Tower(s) for s in structures]
	lookup = {s.name: s for s in towers}
	for s in towers:
		s.link(lookup)

	tower = towers[0]
	while tower.parent:
		tower = tower.parent
	return tower

def find_bottom(structures):
	return construct(structures).name

if __name__ == '__main__':
	main()
