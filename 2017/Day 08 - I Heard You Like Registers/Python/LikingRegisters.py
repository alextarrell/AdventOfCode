#! /usr/bin/env python
# Day 8 - I Heard You Like Registers

import sys
sys.path.append("../../..")

from python_util import prints, get_input
import re
from collections import defaultdict

re_struct = re.compile(r"(\w+) (inc|dec) ((?:-)?\d+) if (\w+) (<|<=|==|!=|>=|>) ((?:-)?\d+)")

def main():
	sample = [
		"b inc 5 if a > 1",
		"a inc 1 if b < 5",
		"c dec -10 if a >= 1",
		"c inc -20 if c == 10"
	]

	print "*** Part 1 ***"
	prints(sample, get_max_reg, 1)
	prints(get_input(), get_max_reg)
	
	print "*** Part 2 ***"
	prints(sample, track_max_reg, 10)
	prints(get_input(), track_max_reg)

def get_max_reg(instructions):
	registers = defaultdict(int)
	for line in instructions:
		compute(line, registers)
	return max(registers.values())

def track_max_reg(instructions):
	registers = defaultdict(int)
	mx = None
	for line in instructions:
		compute(line, registers)
		local_max = max(registers.values())
		if local_max > mx:
			mx = local_max
	return mx

cond_lookup = {
	'<': (lambda t, v: t < v),
	'<=': (lambda t, v: t <= v),
	'==': (lambda t, v: t == v),
	'!=': (lambda t, v: t != v),
	'>=': (lambda t, v: t >= v),
	'>': (lambda t, v: t > v)
}

def compute(line, registers):
	match = re_struct.match(line)
	if not match:
		raise Exception("Failed to parse " + line)

	target = match.group(1)
	op = match.group(2)
	amount = int(match.group(3))
	cond_val = registers[match.group(4)]
	cond = match.group(5)
	cond_amount = int(match.group(6))

	if cond_lookup[cond](cond_val, cond_amount):
		if op == 'inc':
			registers[target] += amount
		elif op == 'dec':
			registers[target] -= amount
		else:
			raise Exception("Unknown operator " + op)

	return registers

if __name__ == '__main__':
	main()
