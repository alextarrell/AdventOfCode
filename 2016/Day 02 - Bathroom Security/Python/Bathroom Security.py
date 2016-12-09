#! /usr/bin/env python
# Day 2 - Bathroom Security

def clamp(val, low, high):
    return max(min(high, val), low)

def main():
	directions = get_input()

	code = []
	x, y = 1, 1
	for line in directions:
		for i in line:
			if i == 'U':
				y -= 1
			elif i == 'D':
				y += 1
			elif i == 'L':
				x -= 1
			elif i == 'R':
				x += 1

			x = clamp(x, 0, 2)
			y = clamp(y, 0, 2)

		code.append(str(y * 3 + x + 1))

	print "The bathroom code is: {}".format(''.join(code))


def get_input():
	with open('../day_2_input.txt') as stats:
		return [s.strip() for s in stats]


if __name__ == "__main__":
	main()
