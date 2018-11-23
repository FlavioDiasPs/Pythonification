
# this wont execute with a generator, so it is not lazy
items = [x * x for x in range(100)]
for item in items:
    print(item)

# this produces a generator, and executes it on demand, so it costs almost no memory
items = (x * x for x in range(100))
for item in items:
    print(item)

# this produces a generator, and executes it on demand, so it costs almost no memory
a = sum(x * x for x in range(100))
print(a)
