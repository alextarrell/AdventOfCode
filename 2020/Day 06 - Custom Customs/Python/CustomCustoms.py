# Day 6 - Custom Customs
import sys

def parse_input(data):
	groups = []
	buf = []
	for line in data:
		if line:
			buf.append(set(line))
		elif buf:
			groups.append(buf)
			buf = []

	if buf:
		groups.append(buf)

	return groups

def uniqs(responses):
	return set().union(*responses)

def main():
	data = (line.strip() for line in sys.stdin.readlines())

	groups = parse_input(data)
	print(sum(len(uniqs(r)) for r in groups))

if __name__ == '__main__':
	main()
