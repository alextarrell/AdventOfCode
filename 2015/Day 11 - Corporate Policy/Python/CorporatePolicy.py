#! /usr/bin/env python
# Day 11 - Corporate Policy

import re, string

trpl = re.compile(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz')
def req_1(password):
	return bool(trpl.search(password))

iol = re.compile(r'i|o|l')
def req_2(password):
	return not bool(iol.search(password))

tp = re.compile(r'(\w)\1.*(\w)\2')
def req_3(password):
	return bool(tp.search(password))

def roll_letter(letter):
	return 'a' if letter == 'z' else string.ascii_lowercase[ord(letter)-96]

def gen_passwords(inpt, validators=[]):
	password = inpt
	while True:
		# The following is terrible. Please don't judge me...
		temp = []
		for i, l in enumerate(password[::-1]):
			temp.append(roll_letter(l))
			if temp[i] != 'a':
				break
		password = ''.join(list(password[:-len(temp)]) + temp[::-1])

		if not validators or all(v(password) for v in validators):
			yield password

def main():
	password_generator = gen_passwords('cqjxjnds', [req_1, req_2, req_3])

	print next(password_generator)
	print next(password_generator)

if __name__ == "__main__":
	main()
