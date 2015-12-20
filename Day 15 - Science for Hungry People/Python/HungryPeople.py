#! /usr/bin/env python
# Day 15 - Science for Hungry People

import re
from collections import namedtuple, Counter
from itertools import combinations_with_replacement

Ingredient = namedtuple('Ingredient', 'name, capacity, durability, flavor, texture, calories')

def score_recipe(recipe, ingredients, calorie_target=0):
	totals = [
		sum(recipe[i]*i.capacity for i in ingredients if i in recipe),
		sum(recipe[i]*i.durability for i in ingredients if i in recipe),
		sum(recipe[i]*i.flavor for i in ingredients if i in recipe),
		sum(recipe[i]*i.texture for i in ingredients if i in recipe),
		sum(recipe[i]*i.calories for i in ingredients if i in recipe),
	]
	if calorie_target > 0 and totals[4] != calorie_target:
		return 0, recipe
	return reduce(lambda x, y: x*y if y > 0 else 0, totals[:4]), recipe

rp = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
def main():
	stats = get_input()
	ingredients = [Ingredient(*map(try_int, rp.match(s).groups())) for s in stats]

	recipes = [dict(Counter(p).most_common()) for p in combinations_with_replacement(ingredients, 100)]
	best = max((score_recipe(r, ingredients) for r in recipes))
	print 'The Optimal Recipe has a score of {} pts'.format(best[0])
	for k, v in best[1].iteritems():
		print '\t{}: {}'.format(k.name, v)

	best = max((score_recipe(r, ingredients, 500) for r in recipes))
	print 'The Optimal Recipe has a score of {} pts and only 500 calories'.format(best[0])
	for k, v in best[1].iteritems():
		print '\t{}: {}'.format(k.name, v)

def get_input():
	with open('../day_15_input.txt') as stats:
		return [s.strip() for s in stats]

def try_int(inpt):
	try:
		return int(inpt)
	except ValueError:
		return inpt

if __name__ == "__main__":
	main()
