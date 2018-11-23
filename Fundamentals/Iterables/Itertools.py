from itertools import islice, count
from Fundamentals.functions import is_even

# COUNT RETURNS AN ITERATOR USING LAZYNESS
t_evens = islice((x for x in count() if is_even(x)), 100)
list(t_evens)

sum(islice((x for x in count() if is_even(x)), 1000))

any([False, True, False])
all([False, True, False])

any(is_even(x) for x in range(0, 1))

any(name[0].upper() == "a".upper() for name in ["Flavio","Dias","Pegas","Alguma coisa"])



#NOT LAZY WAY ----------------------------------------------------
monday = [1, 2, 4, 6, 7, 9, 0]
tuesday = [20, 45, 76, 12, 87]
wednesday = [12, 34, 56, 78]

# converts into list of tuples
# all tuples must have same amount of numbers
# the calculation is made tuple by tuple on the loop
# HOWEVER, THIS IS NOT LAZY, THUS IT IS MEMORY EXPENSIVE
for temps in zip(monday, tuesday, wednesday): 
    print("min={:4.1f}, max={:4.1f}, avg={:4.1f}".format(min(temps), max(temps), sum(temps) / len(temps)))


#CONVERTS TO ALL TOGETHER TO A LIST ----------------------------------------------------
from itertools import chain
monday = [1, 2, 4, 6, 7, 9, 0]
tuesday = [20, 45, 76, 6, 12, 87]
wednesday = [12, 34, 56, 6, 78]
list(chain(monday, tuesday, wednesday))
for temps in chain(monday, tuesday, wednesday):
    print("min={:4.1f}, max={:4.1f}, avg={:4.1f}".format(min(temps), max(temps), sum(temps) / len(temps))) 

