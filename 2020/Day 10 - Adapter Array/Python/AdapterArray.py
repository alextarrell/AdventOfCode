# Day 10 - Adapter Array
import sys

def main():
	data = [int(line.strip()) for line in sys.stdin.readlines()]

	device = max(data) + 3
	data = sorted(data)
	# diff all adjacent elements, count instances of 1 and 3
	# print(solve(data + [device]))


if __name__ == '__main__':
	main()
