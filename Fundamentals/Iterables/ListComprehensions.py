from math import factorial
'''It shows how to deal with iterables in a pythonic way
'''

# LIST
words = "Why should I try to do that when I cna do this".split()
list = [len(word) for word in words]  # it is just a list
type(list)
list

# SET
set = {len(str(factorial(x))) for x in range(20)}  # it is just a set
type(set)  # it removes all repetitious data
set

# DICTIONARY
from pprint import pprint as pp

country_to_capital = {
    'United kingdom': 'London',
    'Brazil': 'Brazilia',
    'Morocco': 'Rabat',
    'Sweden': 'Stockholm',
 }

# key:value expr
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)


from Fundamentals.functions import is_even
[x for x in range(101) if is_even(x)]

# DOING OPERATIONS
valor = {x*x:(x, x+x) for x in range(101) if is_even(x)}
pp(valor)