# Day 1 - Report Repair
import sys

def find_sum(data, target):
	start = 0
	end = len(data) - 1
	while start < end:
		total = data[start] + data[end]
		if total > target:
			end -= 1
		elif total < target:
			start += 1
		else:
			break
	else:
		return None

	return (data[start], data[end])

def main():
	data = sorted(int(line) for line in sys.stdin.readlines())

	result = find_sum(data, 2020)
	if not result:
		print('No Solution')
	else:
		print(result[0] * result[1])

if __name__ == '__main__':
	main()
