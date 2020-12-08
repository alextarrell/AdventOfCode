# Day 3 - Toboggan Trajectory
import functools
import operator
import sys

def traverse(data, slopeX, slopeY):
	trees = 0
	xPos = 0
	yPos = 0
	while yPos < len(data):
		if data[yPos][xPos] == '#':
			trees += 1
		xPos = (xPos + slopeX) % len(data[yPos])
		yPos = yPos + slopeY
	return trees

def main():
	data = [d.strip() for d in sys.stdin.readlines()]

	results = [
		traverse(data, 1, 1),
		traverse(data, 3, 1),
		traverse(data, 5, 1),
		traverse(data, 7, 1),
		traverse(data, 1, 2),
	]

	print(results[1])
	print(functools.reduce(operator.mul, results, 1))

if __name__ == '__main__':
	main()
