"""Um pouquinho sobre tupla

Usage:
    Selecione a shift + enter
"""

def getTupleMinMax(items):
    return (min(items), max(items))

item = [43, 1, 23, 65, 87, 23]

lower, upper = getTupleMinMax(item)
print(lower)
print(upper)

item = getTupleMinMax(item)
print(item)

print(tuple("Flavio"))
print(type((1,)))

5 in (3, 5, 17, 257, 6565) #tuple contains 5
2 in (3, 5, 17, 257, 6565) #tuple doe not contain 2