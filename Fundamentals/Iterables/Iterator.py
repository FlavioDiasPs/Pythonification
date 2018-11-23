
def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

first({"1st","2nd","3rd"}) # this starts from the end
first(["1st","2nd","3rd"]) # this starts from the be

first(set()) # on python, whenever it gets to the end of a iterator, and StopIteration error raises.


##GENERATORS ----------------------------

def myGenerator():
    print("about to yield 1")
    yield 1
    print("about to yield 2")
    yield 2
    print("about to yield 3")
    yield 3
    print("about to yield 4")
    yield 4
    print("return")


# for x in myGenerator():
#     print(x)

gen = myGenerator()
next(gen)   #1
next(gen)   #2
next(gen)   #3
next(gen)   #4
# exception
 