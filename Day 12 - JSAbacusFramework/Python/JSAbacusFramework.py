#! /usr/bin/env python
# Day 12 - JSAbacusFramework.io

import re

nf = re.compile(r'(-?\d+)')
def main():
	json_doc = get_input()

	total = 0
	for m in nf.finditer(json_doc):
		total += int(m.group(1))

	print total

def get_input():
	with open('../day_12_input.txt') as json_doc:
		return json_doc.read()

if __name__ == "__main__":
	main()
