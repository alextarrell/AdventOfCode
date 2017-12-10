#! /usr/bin/env python

import inspect, os

def getCallerPath():
	f = __file__.replace('.pyc', '.py')
	return next((item[1] for item in inspect.stack() if item and f not in item[1]), f)

def get_input(filename=None):
	input_file = None
	if filename:
		input_file = os.path.join(os.path.dirname(getCallerPath()), filename)
	else:
		base_path = os.path.join(os.path.dirname(getCallerPath()), '..')
		input_file = next((os.path.join(base_path, p) for p in os.listdir(base_path) if os.path.basename(p).endswith('_input.txt')), None)

	if not input_file or not os.path.isfile(input_file):
		raise Exception("No input file found!")

	with open(input_file) as data:
		return [d.strip() for d in data]

def prints(data, solver, solution=None):
	result = solver(data)
	if solution is not None:
		if result == solution:
			print "SUCCESS: {} ==> {}".format(data, solution)
		else:
			print "FAIL: {} ==> {} (Expected {})".format(data, result, solution)
	else:
		print "Solution: {}".format(result)
