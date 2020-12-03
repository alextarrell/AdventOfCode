#! /usr/bin/env python
# Day 8 - Two-Factor Authentication

import re

r_rect = re.compile(r'rect (\d+)x(\d+)')
r_rotate = re.compile(r'rotate (?:column|row) (x|y)=(\d+) by (\d+)')

class Screen(object):
	def __init__(self, width, height):
		super(Screen, self).__init__()

		self.grid = [[0 for w in range(width)] for h in range(height)]
		self.width = width
		self.height = height

	def rect(self, width, height):
		for h in range(height):
			for w in range(width):
				self.grid[h][w] = 1

	def rotateCol(self, column, amount):
		rot = [row[column] for row in self.grid]
		amount = amount % len(rot)
		rot = rot[-amount:] + rot[:-amount]
		for idx, row in enumerate(self.grid):
			row[column] = rot[idx]

	def rotateRow(self, row, amount):
		rot = self.grid[row]
		amount = amount % len(rot)
		rot = rot[-amount:] + rot[:-amount]
		self.grid[row] = rot

	def litPixels(self):
		return sum(sum(row) for row in self.grid)

	def __str__(self):
		return "\n".join("".join('#' if v else '.' for v in row) for row in self.grid)

def main():
	directions = get_input()

	scr = Screen(50, 6)
	for d in directions:
		match = r_rect.match(d)
		if match:
			scr.rect(int(match.group(1)), int(match.group(2)))

		match = r_rotate.match(d)
		if match and match.group(1) == 'x':
			scr.rotateCol(int(match.group(2)), int(match.group(3)))
		elif match and match.group(1) == 'y':
			scr.rotateRow(int(match.group(2)), int(match.group(3)))

		print(scr)
		print()

	print("The Screen contains {} lit pixels".format(scr.litPixels()))

def get_input():
	with open('../day_8_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
