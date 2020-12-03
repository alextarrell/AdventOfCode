#! /usr/bin/env python
# Day 1 - Inverse Captcha

import sys
sys.path.append("../../..")

from python_util import prints, get_input

def main():
	print("\n*** Part 1 ***\n")
	prints('1122', solve_next, 3)
	prints('1111', solve_next, 4)
	prints('1234', solve_next, 0)
	prints('91212129', solve_next, 9)
	for captcha in get_input():
		prints(captcha, solve_next)

	print("\n*** Part 2 ***\n")
	prints ('1212', solve_mid, 6)
	prints ('1221', solve_mid, 0)
	prints ('123425', solve_mid, 4)
	prints ('123123', solve_mid, 12)
	prints ('12131415', solve_mid, 4)
	for captcha in get_input():
		prints(captcha, solve_mid)

def solve_next(captcha):
	return sum(int(c) for idx, c in enumerate(captcha) if c == captcha[(idx + 1) % len(captcha)])

def solve_mid(captcha):
	return sum(int(c) for idx, c in enumerate(captcha) if c == captcha[(idx + len(captcha) / 2) % len(captcha)])

if __name__ == '__main__':
	main()
