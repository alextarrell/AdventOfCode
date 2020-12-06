# Day 2 - Password Philosophy
import sys
import re

def is_valid(line):
	m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
	if not m:
		return False

	minOccurs, maxOccurs, letter, password = m.groups()
	occurs = password.count(letter)
	return occurs >= int(minOccurs) and occurs <= int(maxOccurs)

def main():
	data = sys.stdin.readlines()

	valid_count = 0
	for line in data:
		if is_valid(line):
			valid_count += 1

	print(valid_count)

if __name__ == '__main__':
	main()
