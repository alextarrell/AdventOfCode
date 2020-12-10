# Day 5 - Binary Boarding
import sys
import math
from collections import namedtuple

class Seat(namedtuple('SeatBase', ('row', 'column'))):
	@property
	def id(self):
		return self.row * 8 + self.column

def decode(coords, rows, cols):
	st = int(math.log(rows, 2))
	row = int(coords[:st].replace('F', '0').replace('B', '1'), 2)
	column = int(coords[st:].replace('L', '0').replace('R', '1'), 2)
	return Seat(row, column)

def main():
	data = (line.strip() for line in sys.stdin.readlines())

	seats = [decode(row, 128, 8) for row in data]
	print(max(s.id for s in seats))

if __name__ == '__main__':
	main()
