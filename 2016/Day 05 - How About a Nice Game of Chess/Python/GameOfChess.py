#! /usr/bin/env python
# Day 5 - How About a Nice Game of Chess?

from hashlib import md5
from itertools import islice, count, chain

class CachedGenerator(object):
    def __init__(self, iterator):
        self._iter = iter(iterator)
        self.cache = []

    def __iter__(self):
        return chain(self.cache, self._gen_iter())

    def _gen_iter(self):
        for val in self._iter:
            self.cache.append(val)
            yield val

def gen_hash(base, i):
	return md5(base + str(i)).hexdigest()

def main():
	doors = get_input()

	for door in doors:
		hash_generator = CachedGenerator(gen_hash(door, i) for i in count() if gen_hash(door, i)[:5] == '00000')
		hashs = list(islice(hash_generator, 8))
		print 'The password for door ID {} is {}'.format(door, ''.join(h[5] for h in hashs))

		password = list('_' * 8)
		gen = iter(hash_generator)
		while '_' in password:
			h = next(gen)
			idx, ch = int(h[5], 16), h[6]
			if idx >= len(password) or password[idx] != '_': continue

			password[idx] = ch
			print ''.join(password)

		print 'The second password is {}'.format(''.join(password))

def get_input():
	with open('../day_5_input.txt') as data:
		return [d.strip() for d in data]


if __name__ == "__main__":
	main()
