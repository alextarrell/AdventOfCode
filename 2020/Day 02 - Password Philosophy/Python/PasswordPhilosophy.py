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

def is_actually_valid(line):
	m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
	if not m:
		return False

	pos1, pos2, letter, password = m.groups()
	pos1 = int(pos1) - 1
	pos2 = int(pos2) - 1

	if password[pos1] == password[pos2]:
		return False
	elif password[pos1] == letter or password[pos2] == letter:
		return True
	else:
		return False

def main():
	data = sys.stdin.readlines()

	valid_count = 0
	for line in data:
		if is_valid(line):
			valid_count += 1

	print(valid_count)

	valid_count = 0
	for line in data:
		if is_actually_valid(line):
			valid_count += 1

	print(valid_count)

if __name__ == '__main__':
	main()
