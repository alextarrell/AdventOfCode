# Day 3 - Toboggan Trajectory
import sys

def traverse(data, slopeX, slopeY):
	trees = 0
	xPos = 0
	yPos = 0
	while yPos < len(data):
		if data[yPos][xPos] == '#':
			trees += 1
		xPos = (xPos + 3) % len(data[yPos])
		yPos += slopeY
	return trees

def main():
	data = [d.strip() for d in sys.stdin.readlines()]
	print(traverse(data, 3, 1))

if __name__ == '__main__':
	main()
