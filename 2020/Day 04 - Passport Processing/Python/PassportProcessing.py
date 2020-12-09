# Day 4 - Passport Processing
import re
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

	return [dict(sorted(p.split(':') for p in r.split(' '))) for r in records]

def has_fields(record):
	required_fields = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
	return required_fields.issubset(record.keys())

def is_valid(record):
	validations = {
		'byr': r'19[2-9][0-9]|200[0-2]',
		'iyr': r'201[0-9]|2020',
		'eyr': r'202[0-9]|2030',
		'hgt': r'(?:15[0-9]|1[6-8][0-9]|19[0-3])cm|(?:59|6[0-9]|7[0-6])in',
		'hcl': r'#[0-9a-f]{6}',
		'ecl': r'amb|blu|brn|gry|grn|hzl|oth',
		'pid': r'[0-9]{9}',
	}

	return all(k in record and re.fullmatch(p, record[k]) for k, p in validations.items())

def main():
	data = (line.strip() for line in sys.stdin.readlines())

	records = parse_records(data)
	print([has_fields(r) for r in records].count(True))
	print([is_valid(r) for r in records].count(True))

if __name__ == '__main__':
	main()
