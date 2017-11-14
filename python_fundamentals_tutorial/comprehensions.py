import os
import glob
from math import factorial, sqrt
from pprint import pprint as pp

# List Comprehension
f = [len(str(factorial(x))) for x in range(20)]

# Set Comprehension
s = {len(str(factorial(x))) for x in range(20)}

# Dictionary Comprehension
country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brasília',
                      'Marocco': 'Rabat',
                      'Sweden': 'Stockholm'}

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)

words = ['dog', 'party', 'banana', 'ruby']
letter_as_key = {x[0]: x for x in words}
pp(letter_as_key)

# Almost to complex for comprehension
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)

# Filtering with function
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

prime_numbers = [x for x in range(101) if is_prime(x)]
prime_square_divisors = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}
pp(prime_square_divisors)