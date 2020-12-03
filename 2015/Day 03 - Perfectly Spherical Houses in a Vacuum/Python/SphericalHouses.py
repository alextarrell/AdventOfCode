#! /usr/bin/env python
# Day 3 - Perfectly Spherical Houses in a Vacuum

def navigate(x, y, nav):
	if nav == '^':
		return x, y-1
	elif nav == 'v':
		return x, y+1
	elif nav == '<':
		return x-1, y
	elif nav == '>':
		return x+1, y
	else:
		raise ValueError('Invalid Direction: ' + nav)

def visit_houses(directions):
	visited = {(0, 0): 1}
	x, y = 0, 0
	for d in directions:
		try:
			x, y = navigate(x, y, d)
			visited[(x, y)] = visited.get((x, y), 0) + 1
		except ValueError as e:
			print(str(e))
	return visited

def main():
	directions = get_input()

	print('Year 1:')
	print('Santa Visited {} Unique Houses'.format(len(visit_houses(directions))))

	santas_houses = visit_houses(directions[::2])

	robo_santas_houses = visit_houses(directions[1::2])

	joint_houses = santas_houses.copy()
	joint_houses.update(robo_santas_houses)

	print('Year 2:')
	print('Santa Visited {} Unique Houses'.format(len(santas_houses)))
	print('Robo-Santa Visited {} Unique Houses'.format(len(robo_santas_houses)))
	print('Together, they visited {} Unique Houses'.format(len(joint_houses)))

def get_input():
	with open('../day_3_input.txt') as directions:
		return [d.strip() for d in directions][0]

if __name__ == "__main__":
	main()
