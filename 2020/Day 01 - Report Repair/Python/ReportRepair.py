# Day 1 - Report Repair
import sys

def find_duo_sum(data, target):
	if not data or len(data) < 2:
		return None
	elif len(data) == 2:
		return (data[0], data[1]) if sum(data == target) else None

	start = 0
	end = len(data) - 1
	while start < end:
		total = data[start] + data[end]
		if total > target:
			end -= 1
		elif total < target:
			start += 1
		else:
			return (data[start], data[end])

	return None

def find_tri_sum(data, target):
	if not data or len(data) < 3:
		return None
	elif len(data) == 3:
		return (data[0], data[1], data[2]) if sum(data == target) else None

	start = 0
	while start < len(data):
		result = find_duo_sum(data[start:], target - data[start])
		if result:
			return data[start], result[0], result[1]
		else:
			start += 1
	return None

def main():
	data = sorted(int(line) for line in sys.stdin.readlines())

	result = find_duo_sum(data, 2020)
	if not result:
		print('No Solution')
	else:
		print(result[0] * result[1])

	result = find_tri_sum(data, 2020)
	if not result:
		print('No Solution')
	else:
		print(result[0] * result[1] * result[2])

if __name__ == '__main__':
	main()
