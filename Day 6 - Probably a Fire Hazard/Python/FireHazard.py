#! /usr/bin/env python
# Day 6 - Probably a Fire Hazard

import re

def init_lights(width, height, val=False):
	lights = []
	for _ in xrange(height):
		lights.append([val for _ in xrange(width)])
	return lights

def switch(lights, x1, y1, x2, y2, lightsOn):
	for x in xrange(x1, x2):
		for y in xrange(y1, y2):
			lights[x][y] = lightsOn

def toggle(lights, x1, y1, x2, y2):
	for x in xrange(x1, x2):
		for y in xrange(y1, y2):
			lights[x][y] = not lights[x][y]

def add_brightness(lights, x1, y1, x2, y2, amount):
	for x in xrange(x1, x2):
		for y in xrange(y1, y2):
			val = lights[x][y] + amount
			lights[x][y] = val if val > 0 else 0

ad = re.compile(r'([ a-z]+) (\d+),(\d+) through (\d+),(\d+)')
def apply_direction(lights, direction, v2=False):
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
			if v2:
				add_brightness(lights, x1, y1, x2+1, y2+1, 1)
			else:
				switch(lights, x1, y1, x2+1, y2+1, True)
		elif action == 'turn off':
			if v2:
				add_brightness(lights, x1, y1, x2+1, y2+1, -1)
			else:
				switch(lights, x1, y1, x2+1, y2+1, False)
		elif action == 'toggle':
			if v2:
				add_brightness(lights, x1, y1, x2+1, y2+1, 2)
			else:
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

def sum_brightness(lights):
	total = 0
	for x in xrange(len(lights)):
		total += sum(lights[x])
	return total

def main():
	lights = init_lights(1000, 1000)
	directions = get_input()
	for d in directions:
		apply_direction(lights, d)
	print count_lights(lights)

	lights = init_lights(1000, 1000, 0)
	for d in directions:
		apply_direction(lights, d, True)
	print sum_brightness(lights)

def get_input():
	with open('../day_6_input.txt') as directions:
		return [d.strip() for d in directions]

if __name__ == "__main__":
	main()
