# Day 7 - Handy Haversacks
import sys, re
from collections import namedtuple

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

def main():
	data = (line.strip() for line in sys.stdin.readlines())

	rules = [parse_rule(r) for r in data]
	print(len(can_contain(rules, 'shiny gold')))

if __name__ == '__main__':
	main()
