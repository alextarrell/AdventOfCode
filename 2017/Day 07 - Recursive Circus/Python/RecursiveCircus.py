#! /usr/bin/env python
# Day 7 - Recursive Circus

import sys
sys.path.append("../../..")

from python_util import prints, get_input
import re
from collections import Counter

re_struct = re.compile(r"(\w+) \((\d+)\)(?: -> (.*))?")

class Tower():
	def __init__(self, structure):
		match = re_struct.match(structure)
		self.name = match.group(1)
		self._weight = int(match.group(2))
		self.subs = [_f for _f in (match.group(3) or "").split(', ') if _f]
		self.parent = None

	def link(self, lookup):
		self.subs = [lookup[sub] for sub in self.subs]
		for tower in self.subs:
			tower.parent = self

	def weight(self):
		if not hasattr(self, '__weight'):
			setattr(self, '__weight', self._weight + sum(tower.weight() for tower in self.subs))
		return getattr(self, '__weight')

	def balanced(self):
		return all(self.subs[0].weight() == s.weight() for s in self.subs)

	def __str__(self):
		if self.subs:
			return "{} ({}) -> [{}]".format(self.name, self._weight, ', '.join(str(s) for s in self.subs))
		else:
			return "{} ({})".format(self.name, self._weight)
	__repr__ = __str__

def main():
	print("*** Part 1 ***")

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

	print("*** Part 2 ***")
	prints(sample, find_imbalance, 60)
	prints(get_input(), find_imbalance)

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

def find_imbalance(structures):
	tower = construct(structures)
	while not tower.balanced():
		if all(s.balanced() for s in tower.subs):
			break
		tower = next(s for s in tower.subs if not s.balanced())
	target, imbalance = tuple(c[0] for c in Counter(s.weight() for s in tower.subs).most_common())
	imbalanced_tower = next(s for s in tower.subs if s.weight() == imbalance)
	return imbalanced_tower._weight + target - imbalance

if __name__ == '__main__':
	main()
