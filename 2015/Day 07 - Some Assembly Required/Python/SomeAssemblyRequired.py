#! /usr/bin/env python
# Day 7 - Some Assembly Required

import re

class Wire():
	def __init__(self, circuit, left, right=None, operator=None):
		self.circuit = circuit
		self.left_operand = left
		self.right_operand = right
		self.operator = operator

	def eval_operand(self, operand):
		try:
			return int(operand)
		except:
			return self.circuit[operand].val()

	def left(self):
		return self.eval_operand(self.left_operand)

	def right(self):
		return self.eval_operand(self.right_operand)

	def val(self):
		if not hasattr(self, '_val'):
			if not self.operator:
				setattr(self, '_val', self.right())
			elif self.operator == 'AND':
				setattr(self, '_val', self.left() & self.right())
			elif self.operator == 'OR':
				setattr(self, '_val', self.left() | self.right())
			elif self.operator == 'LSHIFT':
				setattr(self, '_val', self.left() << self.right())
			elif self.operator == 'RSHIFT':
				setattr(self, '_val', self.left() >> self.right())
			elif self.operator == 'NOT':
				setattr(self, '_val', ~self.right())
			else:
				raise ValueError('Invalid Operator: ' + self.operator)
		return getattr(self, '_val')

	def reset(self):
		if hasattr(self, '_val'):
			delattr(self, '_val')

pd = re.compile(r'(?:(\w+) )??(?:(\w+) )?(\w+) -> (\w+)')
def add_component(circuit, direction):
	m = pd.match(direction)
	if m:
		left_operand = m.group(1)
		operator = m.group(2)
		right_operand = m.group(3)
		identifier = m.group(4)

		part = Wire(circuit, left_operand, right_operand, operator)
		circuit[identifier] = part
	else:
		print('Could not parse direction', direction)

def main():
	directions = get_input()

	circuit = {}
	for d in directions:
		add_component(circuit, d)

	print(circuit['a'].val())

	circuit['b'].right_operand = circuit['a'].val()
	[v.reset() for v in circuit.values()]
	print(circuit['a'].val())

def get_input():
	with open('../day_7_input.txt') as directions:
		return [d.strip() for d in directions]

if __name__ == "__main__":
	main()
