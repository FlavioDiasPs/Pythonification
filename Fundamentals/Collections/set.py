
#set is a list of unique values
#do not preserver order

#declaration
p = {6, 4, 53645, 785565}

a = {}  # this is a empty dictionary
b = set()  # this is a empty set


c = set([2, 4, 16, 64, 4, 4096])
c  # removes duplicated

#checks, adds, deletes
2 in c
2 not in c
c.add(1324356)
c.remove(2)
c.discard(3)
c.update([2, 3, 6, 8])
c

#COPYING
d = c.copy()
e = set(d)

#SET IN ALGEBRA
a = {1, 2, 3}
b = {2, 3, 4}
c = {2, 3}
d = {4, 5}

a.union(b)
a.intersection(b)
a.difference(b)  # exists in a but not exists in b
a.symmetric_difference(b)  # exists in a but not exists on b and the oposite
c.issubset(a)  # c is subset of a, it means that a contains all c items
a.issuperset(c)  # oposite of above
a.isdisjoint(d)  # nothing in commom
