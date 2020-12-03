#! /usr/bin/env python
# Day 2 - I Was Told There Would Be No Math

def wrapping_area(x, y, z):
	side_areas = [x*y, x*z, y*z]
	return 2 * sum(side_areas) + min(side_areas)

def ribbon_length(x, y, z):
	perims = [2*(x+y), 2*(x+z), 2*(y+z)]
	return min(perims) + x*y*z

def main():
	presents_list = get_input()

	total_area = 0
	total_length = 0
	for present_dim in presents_list:
		dims = [int(d) for d in present_dim.split('x')]
		total_area += wrapping_area(*dims)
		total_length += ribbon_length(*dims)
	print('{} ft^2 of wrapping paper'.format(total_area))
	print('{} ft of ribbon'.format(total_length))

def get_input():
	with open('../day_2_input.txt') as directions:
		return [d.strip() for d in directions]

if __name__ == "__main__":
	main()
