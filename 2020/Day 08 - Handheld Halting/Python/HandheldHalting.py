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
			break
		trail.add(ip)
		ip, acc = step(program[ip], ip, acc)
	return acc

def main():
	data = [line.strip() for line in sys.stdin.readlines()]

	print(run_program(data))

if __name__ == '__main__':
	main()
