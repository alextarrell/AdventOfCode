# Day 7 - Handy Haversacks
import sys, re
from collections import defaultdict, namedtuple

Rule = namedtuple('Rule', ('color', 'contents'))
def parse_rule(rule):
	m = re.findall(r'(?:(\d+) )?(\w+ \w+) bags?', rule)
	return Rule(m[0][1], {g[1]: int(g[0]) for g in m[1:] if g[0]})

def can_contain(rules, color):
	allowed = set()
	for rule in rules:
		if color in rule.contents:
			allowed.add(rule.color)
			allowed.update(can_contain(rules, rule.color))
	return allowed

def nested_bags(rules, color):
	rule = next(r for r in rules if r.color == color)
	contained = defaultdict(int, **rule.contents)
	for c, n in rule.contents.items():
		for ci, ni in nested_bags(rules, c).items():
			contained[ci] += ni * n

	return contained

def main():
	data = (line.strip() for line in sys.stdin.readlines())

	rules = [parse_rule(r) for r in data]
	print(len(can_contain(rules, 'shiny gold')))
	print(sum(nested_bags(rules, 'shiny gold').values()))

if __name__ == '__main__':
	main()
