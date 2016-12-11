#! /usr/bin/env python
# Day 3 - Squares With Three Sides

def main():
	triangles = get_input()

	valid = [verts for verts in triangles if 2 * max(verts) < sum(verts)]

	print "Of the {} listed triangles, {} are possible".format(len(triangles), len(valid))

def get_input():
	with open('../day_3_input.txt') as triangles:
		return [[int(r) for r in s.split()] for s in triangles]


if __name__ == "__main__":
	main()
