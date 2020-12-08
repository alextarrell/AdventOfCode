# Day 4 - Passport Processing
import sys

def parse_records(data):
	records = []
	buf = []
	for line in data:
		if line:
			buf.append(line.strip())
		else:
			records.append(' '.join(buf))
			buf = []
	if buf:
		records.append(' '.join(buf))

	return [dict(p.split(':') for p in r.split(' ')) for r in records]

def is_valid(record):
	required_fields = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
	return required_fields.issubset(record.keys())

def main():
	data = (line.strip() for line in sys.stdin.readlines())

	records = parse_records(data)
	print([is_valid(r) for r in records].count(True))

if __name__ == '__main__':
	main()
