
range(5)
list(range(5, 10))  # the end is excluded
list(range(10, 15))  # makes sense when dealing with progressive things

list(range(10, 15, 2))  # we can use with steps

v = [2, 45, 765, 23]
for i in v:
    print(i)


def iterateOverList():
    s = [0, 1, 4, 6, 13]
    for v in s:
        print(v)


iterateOverList()


def iterateOverTuple():
    s = [0, 1, 4, 6, 13]
    for v in enumerate(s):
        print(v)


iterateOverTuple()

#this is the better way to iterate over a list
#it is iterating over a primitive object made for it
#it gives you i->index and v-> value


def iterateOverUnpacketTuple():
    s = [0, 1, 4, 6, 13]    
    for i, v in enumerate(s):
        print("{}, {}".format(i, v))


iterateOverUnpacketTuple()
