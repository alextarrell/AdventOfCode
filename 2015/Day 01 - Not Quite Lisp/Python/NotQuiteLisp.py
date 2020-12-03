#! /usr/bin/env python
# Day 1 - Not Quite Lisp

def pather(directions):
	pos = 0
	for d in directions:
		if d == '(':
			pos += 1
		elif d == ')':
			pos -= 1
	return pos

def basement_finder(directions):
	pos = 0
	for index, d in enumerate(directions):
		if d == '(':
			pos += 1
		elif d == ')':
			pos -= 1

		if pos < 0:
			return index+1

def main():
	directions = get_input()
	print(pather(directions))
	print(basement_finder(directions))

def get_input():
	with open('../day_1_input.txt') as directions:
		return [d.strip() for d in directions][0]

if __name__ == "__main__":
	main()
