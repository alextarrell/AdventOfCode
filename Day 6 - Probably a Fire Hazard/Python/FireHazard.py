#! /usr/bin/env python
# Day 6 - Probably a Fire Hazard

import re

def init_lights(width, height):
	lights = []
	for _ in xrange(height):
		lights.append([False for _ in xrange(width)])
	return lights

def switch(lights, x1, y1, x2, y2, lightsOn):
	for x in xrange(x1, x2):
		for y in xrange(y1, y2):
			lights[x][y] = lightsOn

def toggle(lights, x1, y1, x2, y2):
	for x in xrange(x1, x2):
		for y in xrange(y1, y2):
			lights[x][y] = not lights[x][y]

ad = re.compile(r'([ a-z]+) (\d+),(\d+) through (\d+),(\d+)')
def apply_direction(lights, direction):
	if not direction:
		return

	m = ad.match(direction)
	if m:
		action = m.group(1)
		x1 = int(m.group(2))
		y1 = int(m.group(3))
		x2 = int(m.group(4))
		y2 = int(m.group(5))

		if action == 'turn on':
			switch(lights, x1, y1, x2+1, y2+1, True)
		elif action == 'turn off':
			switch(lights, x1, y1, x2+1, y2+1, False)
		elif action == 'toggle':
			toggle(lights, x1, y1, x2+1, y2+1)
		else:
			raise ValueError('Unknown Action: ' + action)
	else:
		raise ValueError('Could Not Parse Direction: ' + direction)

def count_lights(lights):
	total = 0
	for x in xrange(len(lights)):
		for y in xrange(len(lights[x])):
			if lights[x][y]:
				total += 1
	return total

def main():
	lights = init_lights(1000, 1000)
	directions = get_input()
	for d in directions:
		apply_direction(lights, d)
	print count_lights(lights)

def get_input():
	with open('../day_6_input.txt') as directions:
		return [d.strip() for d in directions]

if __name__ == "__main__":
	main()
