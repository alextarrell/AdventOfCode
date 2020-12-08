#! /usr/bin/env python
from collections import namedtuple
from pathlib import Path
import argparse
import re
import shlex
import subprocess

stream = False

def parse_args(args=None):
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	years = sorted((p.name for p in Path().glob('*') if p.is_dir() and re.match(r'\d{4}', p.name)), key=lambda y: int(y))
	languages = sorted(m.group(1) for v in globals() if (m := re.match(r'run_(\w+)_solution', v)))

	parser.add_argument('-d', '--day', type=int, help='Target Day')
	parser.add_argument('-y', '--year', type=str, help='Target Year', choices=years, default=years[-1])
	parser.add_argument('-l', '--language', help='Target Language. If only one is available for the given problem it will be used automatically', choices=languages)
	parser.add_argument('--test', action='store_true', help='Runs test cases (if available) instead of solving')
	parser.add_argument('--stream', action='store_true', help='Streams the output in realtime. Useful for debugging issues')

	return parser.parse_args(args)

def get_days(year):
	"""Gets all the days in a given year"""
	def parse_day(p):
		m = re.match(r'[^\-1-9]*(\d+).*', p.name)
		if p.is_dir() and m and m.group(1):
			return (int(m.group(1)), p)

	return {day[0]: day[1] for p in (Path('.') / year).glob('*') if (day := parse_day(p))}

def find_day(year, num=None):
	"""Gets the specified day from a given year otherwise grabs the highest"""
	days = get_days(year)
	if num:
		return days.get(num, None)
	else:
		return days.get(max(days.keys(), default=None), None)

def get_inputs(day):
	return sorted(day.glob('*input*.txt'))

TestCase = namedtuple('TestCase', ('id', 'in_path', 'out_path'))
def get_test_cases(day):
	"""Returns all test cases for a given day"""
	inputs = sorted(day.glob('Tests/input_*.txt'))
	outputs = sorted(day.glob('Tests/output_*.txt'))

	test_cases = {}
	for f in inputs:
		if (m := re.match(r'input_(.*)\.txt', f.name)):
			test_cases[m.group(1)] = TestCase(m.group(1), f, None)

	for f in outputs:
		if (m := re.match(r'output_(.*)\.txt', f.name)):
			if m.group(1) in test_cases:
				tc = test_cases[m.group(1)]
				test_cases[tc.id] = TestCase(tc.id, tc.in_path, f)
			else:
				test_cases[m.group(1)] = TestCase(m.group(1), None, f)

	return sorted(test_cases.values())

CommandResult = namedtuple('CommandResult', ('returncode', 'result'))
def shrun(command, stdin=None, **kwargs):
	if isinstance(command, str):
		command = shlex.split(command)
	else:
		command = [str(c) for c in command]

	process = subprocess.Popen(
		command,
		stdin=subprocess.PIPE if stdin else None,
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT,
		text=True,
		**kwargs
	)

	if stdin:
		process.stdin.write(stdin)
		process.stdin.close()

	returncode = None
	result = []
	while True:
		if line := process.stdout.readline():
			line = line.rstrip()
			if stream:
				print(line)
			result.append(line)

		if (returncode := process.poll()) is not None:
			break

	return CommandResult(returncode, '\n'.join(result))

def run_test(day, lang, test):
	"""Runs a test case and compares with the expected output"""
	print(f'Running Test {test.id}...', end=('\n' if stream else ' '))

	if test.in_path:
		returncode, result = run_solution(day, lang, test.in_path.read_text())
	else:
		returncode, result = run_solution(day, lang)

	expected_output = test.out_path.read_text().rstrip() if test.out_path else ''

	# Run failed with a non-zero returncode
	if returncode != 0:
		print(f'Error! ({returncode})')
		print(result)
		return False

	# Run finished but we're not expecting anything specific
	if not expected_output:
		if len(result) < 15 and '\n' not in result:
			print(f'Done! (Got "{result}")')
		else:
			print('Done!')
			print(result)
		return True

	# Check if the output matches the expected output
	if expected_output == result:
		if len(result) < 15 and '\n' not in result:
			print(f'Pass! (Got "{result}")')
		else:
			print('Pass!')
			print(result)
		return True

	# Everything ran but our expectations were not met
	if len(result) < 15 and len(expected_output) < 15 and '\n' not in result and '\n' not in expected_output:
		print(f'Fail! (Expected "{expected_output}" Got "{result}")')
	else:
		print('Fail!')
		print('Expected:')
		print(expected_output)
		print('Got:')
		print(result)
	return False

def run_solution(day, lang=None, stdin=None):
	if not lang:
		options = set(m.group(1).lower() for v in globals() if (m := re.match(r'run_(\w+)_solution', v)))
		poss = [f for f in day.glob('*') if f.is_dir() and f.name.lower() in options]
		if len(poss) == 0:
			raise ValueError('No languages found')
		elif len(poss) == 1:
			lang = poss[0]
		else:
			raise ValueError('Multiple languages found')

	func_name = f'run_{lang}_solution'.lower()
	if func_name in globals():
		return globals()[func_name](day, stdin)
	else:
		raise ValueError('No support for ' + lang)

def run_python_solution(day, stdin=None):
	"""
	Runs the Python solution for a given day with the supplied input

	Searches under a Python directory for that day. If only a single Python file exists
	that will be used. Otherwise if there's multiple  a `__main__.py` will be preferred,
	with `__init__.py` used as a fallback.
	"""
	files = list((day / 'Python').glob('*.py'))
	if not files:
		raise ValueError('No Python Files Found!')
	elif len(files) == 1:
		target = files[0]
	elif (target := next((f for f in files if f.name == '__main__.py'), None)):
		pass
	elif (target := next((f for f in files if f.name == '__init__.py'), None)):
		pass
	else:
		raise ValueError('Unable to find an entrypoint!')

	return shrun(
		['python', '-u', '-m', f'Python.{target.stem}'],
		stdin=stdin,
		cwd=day
	)

def main(args=None):
	args = parse_args(args)

	day = find_day(args.year, args.day)
	if not day:
		print(f'No such day in year {args.year}')
		return

	lang = args.language or 'Python'

	global stream
	stream = args.stream

	if args.test:
		print(f'{args.year} - {day.name} ({lang})')

		success_count = 0
		test_cases = get_test_cases(day)
		for test in test_cases:
			success_count += run_test(day, lang, test)
		print(f'{success_count} of {len(test_cases)} Test Cases Succeeded!')
	else:
		print(f'{args.year} - {day.name} ({lang})')

		inputs = get_inputs(day)
		if len(inputs) == 0:
			returncode, result = run_solution(day, lang)
			if returncode != 0:
				print(f'Error! ({returncode})')
			if not stream:
				print(result.strip())
		elif len(inputs) == 1:
			returncode, result = run_solution(day, lang, inputs[0].read_text())
			if returncode != 0:
				print(f'Error! ({returncode})')
			if not stream:
				print(result.strip())
		else:
			for idx, i in enumerate(inputs):
				if idx > 0:
					print()
				print(f'Input "{i.stem}":')
				returncode, result = run_solution(day, lang, i.read_text())
				if returncode != 0:
					print(f'Error! ({returncode})')
				if not stream:
					print(result.strip())


if __name__ == '__main__':
	main()
