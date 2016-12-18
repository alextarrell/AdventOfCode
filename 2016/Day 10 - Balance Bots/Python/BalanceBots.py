#! /usr/bin/env python
# Day 10 - Balance Bots

import re

r_command = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)|value (\d+) goes to bot (\d+)')

class Bot(object):
	def __init__(self, num):
		super(Bot, self).__init__()
		self.num = num
		self.low_output = None
		self.high_output = None
		self.low_val = None
		self.high_val = None
		self.history = set()

	def take(self, val):
		val = int(val)
		self.history.add(val)
		existing = self.low_val or self.high_val
		if existing and val < existing:
			self.low_val = val
			self.high_val = existing
		elif existing and val >= existing:
			self.low_val = existing
			self.high_val = val
		else:
			self.low_val = val

		self.process()

	def process(self):
		if self.low_val and self.low_output and self.high_val and self.high_output:
			self.low_output.take(self.low_val)
			self.high_output.take(self.high_val)
			self.low_val = None
			self.high_val = None

	def __str__(self):
		return 'Bot {:>4}: {:>4} < {:>4}  ->  {:>4} & {:>4}, [{}]'.format(
			self.num, self.low_val, self.high_val,
			self.low_output.num if self.low_output else None,
			self.high_output.num if self.high_output else None,
			", ".join(str(h) for h in self.history))

class Output(object):
	def __init__(self, num):
		super(Output, self).__init__()
		self.num = num
		self.content = []

	def take(self, val):
		self.content.append(str(val))

def main():
	commands = get_input()

	bots = {}
	outputs = {}

	def getProcess(t, num):
		if t == 'bot':
			if not bots.get(num):
				bots[num] = Bot(num)
			return bots[num]
		elif t == 'output':
			if not outputs.get(num):
				outputs[num] = Output(num)
			return outputs[num]
		else:
			raise Exception('{} is invalid'.format(t))

	for command in commands:
		match = r_command.match(command)
		if not match:
			raise Exception('Unable to parse "{}"'.format(command))

		if match.group(1):
			bot = getProcess('bot', match.group(1))
			bot.low_output = getProcess(match.group(2), match.group(3))
			bot.high_output = getProcess(match.group(4), match.group(5))
			bot.process()
		elif match.group(6):
			getProcess('bot', match.group(7)).take(match.group(6))
		else:
			raise Exception('wat')

	target = next(b.num for b in bots.itervalues() if 61 in b.history and 17 in b.history)
	print 'Bot {} compares the 61 and 17 microchips'.format(target)

def get_input():
	with open('../day_10_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
