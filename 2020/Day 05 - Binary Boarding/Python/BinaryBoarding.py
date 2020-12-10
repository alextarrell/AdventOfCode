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

def find_seat(seats):
	if len(seats) < 3:
		return None

	seats = sorted(s.id for s in seats)
	lookup = set(seats)
	for _id in range(seats[1], seats[-1]):
		if _id not in lookup:
			return Seat(int(_id / 8), _id % 8)
	return None

def main():
	data = (line.strip() for line in sys.stdin.readlines())

	seats = [decode(row, 128, 8) for row in data]
	print(max(s.id for s in seats))

	if (seat := find_seat(seats)):
		print(seat.id)
	else:
		print('Not Found')

if __name__ == '__main__':
	main()
