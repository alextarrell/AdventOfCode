#! /usr/bin/env python
# Day 7 - Internet Protocol Version 7

import re

r_mirror = re.compile(r'(\w)(?!\1)(\w)\2\1')
r_in_brackets = re.compile(r'\[([^\[\]]+)\]')
r_out_brackets = re.compile(r'(\w+)(?![^\[]*\])')
def supportsTLS(addr):
	inside = r_in_brackets.findall(addr)
	outside = r_out_brackets.findall(addr)

	return [t for t in outside if r_mirror.search(t)] and not [t for t in inside if r_mirror.search(t)]

def main():
	addresses = get_input()

	valid_addrs = [addr for addr in addresses if supportsTLS(addr)]
	print 'Of the {} IP addresses, {} support TLS'.format(len(addresses), len(valid_addrs))

def get_input():
	with open('../day_7_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
