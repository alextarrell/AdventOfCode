#! /usr/bin/env python
# Day 2 - Bathroom Security

def get_code(start, directions, keypad):
	code = []
	x, y = next(k for k, v in keypad.iteritems() if v == start)
	for line in directions:
		for i in line:
			if i == 'U' and (x, y - 1) in keypad:
				y -= 1
			elif i == 'D' and (x, y + 1) in keypad:
				y += 1
			elif i == 'L' and (x - 1, y) in keypad:
				x -= 1
			elif i == 'R' and (x + 1, y) in keypad:
				x += 1

		code.append(keypad[(x, y)])

	return ''.join(code)

def main():
	directions = get_input()

	# 1 2 3
	# 4 5 6
	# 7 8 9
	keypad = {
		(0, 0): '1',
		(1, 0): '2',
		(2, 0): '3',
		(0, 1): '4',
		(1, 1): '5',
		(2, 1): '6',
		(0, 2): '7',
		(1, 2): '8',
		(2, 2): '9'
	}

	print "The bathroom code is: {}".format(get_code('5', directions, keypad))

	#     1
	#   2 3 4
	# 5 6 7 8 9
	#   A B C
	#     D
	keypad = {
		(2, 0): '1',
		(1, 1): '2',
		(2, 1): '3',
		(3, 1): '4',
		(0, 2): '5',
		(1, 2): '6',
		(2, 2): '7',
		(3, 2): '8',
		(4, 2): '9',
		(1, 3): 'A',
		(2, 3): 'B',
		(3, 3): 'C',
		(2, 4): 'D'
	}

	print "The real bathroom code is: {}".format(get_code('5', directions, keypad))

def get_input():
	with open('../day_2_input.txt') as stats:
		return [s.strip() for s in stats]


if __name__ == "__main__":
	main()
