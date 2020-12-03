#! /usr/bin/env python
# Day 7 - Internet Protocol Version 7

import re

r_mirror = re.compile(r'(\w)(?!\1)(\w)\2\1') # Matches things like 'abba' but not 'aaaa'
r_smirror = re.compile(r'(?=(\w)(?!\1)(\w)\1)') # Matches things like 'aba' but not 'aaa'
r_in_brackets = re.compile(r'\[([^\[\]]+)\]') # Captures everything between []
r_out_brackets = re.compile(r'(\w+)(?![^\[]*\])') # Captures everything not surrounded by []

def supportsTLS(addr):
	inside = r_in_brackets.findall(addr)
	outside = r_out_brackets.findall(addr)

	return [t for t in outside if r_mirror.search(t)] and not [t for t in inside if r_mirror.search(t)]

def supportsSSL(addr):
	inside = r_in_brackets.findall(addr)
	outside = r_out_brackets.findall(addr)

	matches = set(s + f + s for i in inside for f, s in r_smirror.findall(i))
	return any(any(m in o for o in outside) for m in matches)

def main():
	addresses = get_input()

	tls_addrs = [addr for addr in addresses if supportsTLS(addr)]
	ssl_addrs = [addr for addr in addresses if supportsSSL(addr)]
	print('Of the {} IP addresses, {} support TLS and {} support SSL'.format(len(addresses), len(tls_addrs), len(ssl_addrs)))

def get_input():
	with open('../day_7_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
