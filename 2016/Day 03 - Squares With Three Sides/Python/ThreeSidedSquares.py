#! /usr/bin/env python
# Day 3 - Squares With Three Sides

from itertools import chain, islice

def chunk(it, size):
    return iter(lambda: tuple(islice(it, size)), ())

def main():
	triangles = get_input()

	valid_rows = [verts for verts in triangles if 2 * max(verts) < sum(verts)]

	print "Of the {} listed triangles, {} are possible horizontally".format(len(triangles), len(valid_rows))

	valid_verticals = [verts for verts in chunk(chain.from_iterable(zip(*triangles)), 3) if 2 * max(verts) < sum(verts)]

	print "When interpreted vertically, {} are valid".format(len(valid_verticals))

def get_input():
	with open('../day_3_input.txt') as triangles:
		return [[int(r) for r in s.split()] for s in triangles]


if __name__ == "__main__":
	main()
