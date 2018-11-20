"""Um pouquinho sobre tupla

Usage:
    Selecione a shift + enter
"""

def getTupleMinMax(items):
    return (min(items), max(items))

listitem = [43, 1, 23, 65, 87, 23]
tupleitem = (2, 4)

lower, upper = getTupleMinMax(listitem)
print(lower)
print(upper)

listitem = getTupleMinMax(listitem)
print(listitem)

print(tuple("Flavio"))
print(type((1,)))

5 in (3, 5, 17, 257, 6565) #tuple contains 5
2 in (3, 5, 17, 257, 6565) #tuple doe not contain 2