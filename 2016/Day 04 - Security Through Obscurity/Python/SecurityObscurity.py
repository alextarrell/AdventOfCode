#! /usr/bin/env python
# Day 4 - Security Through Obscurity

import re
from collections import Counter

re_parser = re.compile(r'([\w-]+)-(\d+)\[(\w{5})\]')
def parse(room):
	match = re_parser.match(room)
	if not match: raise Exception('Failed to parse: ' + room)

	return {
		'name': match.group(1),
		'sectorId': int(match.group(2)),
		'checksum': match.group(3)
	}

def is_valid_room(room):
	return room['checksum'] == ''.join(f[0] for f in sorted(Counter(room['name'].replace('-', '')).most_common(), key=lambda p: (-p[1], p[0]))[:5])

def main():
	rooms = get_input()

	valid_rooms = filter(is_valid_room, rooms)

	print 'Of the {} rooms, {} were valid and contained a total sectorId of {}'.format(
		len(rooms), len(valid_rooms), sum(r['sectorId'] for r in valid_rooms))

def get_input():
	# return [parse(d) for d in [
	# 	'aaaaa-bbb-z-y-x-123[abxyz]',
	# 	'a-z-y-x-w-l-b-c-d-e-f-g-h-987[abcde]',
	# 	'not-a-real-room-404[oarel]',
	# 	'totally-real-room-200[decoy]'
	# ]]

	with open('../day_4_input.txt') as data:
		return [parse(d.strip()) for d in data]


if __name__ == "__main__":
	main()
