# Day 8 - Handheld Halting
import sys, re

def step(line, ip, acc):
	m = re.fullmatch(r'(nop|acc|jmp) ([+-]\d+)', line)
	if not m:
		raise ValueError(f'Invalid Instruction [{ip}] - {line}')

	ins = m.group(1)
	val = int(m.group(2))

	if ins == 'nop':
		return ip + 1, acc
	elif ins == 'acc':
		return ip + 1, acc + val
	elif ins == 'jmp':
		return ip + val, acc

def run_program(program):
	ip = 0
	acc = 0

	trail = set()
	while True:
		if ip in trail:
			return False, acc
		if ip == len(program):
			return True, acc
		trail.add(ip)
		ip, acc = step(program[ip], ip, acc)

def fix_program(program):
	for idx, line in enumerate(program):
		if 'nop' in line:
			line = line.replace('nop', 'jmp')
		elif 'jmp' in line:
			line = line.replace('jmp', 'nop')
		else:
			continue

		altered = program[:idx] + [line] + program[idx+1:]
		finished, result = run_program(altered)
		if finished:
			return idx, result
	return -1, None


def main():
	data = [line.strip() for line in sys.stdin.readlines()]

	print(run_program(data)[1])
	print(fix_program(data)[1])

if __name__ == '__main__':
	main()
