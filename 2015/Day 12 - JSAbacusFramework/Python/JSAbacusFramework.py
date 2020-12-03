#! /usr/bin/env python
# Day 12 - JSAbacusFramework.io

import json

def sum_node(node, ignore_key=None):
	if isinstance(node, int):
		return node
	elif isinstance(node, str):
		try:
			return int(node)
		except ValueError:
			return 0
	elif isinstance(node, dict):
		if ignore_key and ignore_key in list(node.values()):
			return 0
		else:
			return sum([sum_node(n, ignore_key) for n in node.values()])
	elif isinstance(node, list):
		return sum([sum_node(n, ignore_key) for n in node])
	else:
		return 0

def main():
	json_doc = json.loads(get_input())
	print(sum_node(json_doc))
	print(sum_node(json_doc, 'red'))

def get_input():
	with open('../day_12_input.txt') as json_doc:
		return json_doc.read()

if __name__ == "__main__":
	main()
