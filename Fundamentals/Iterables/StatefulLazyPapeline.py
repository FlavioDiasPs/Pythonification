##STATEFUL GENERATORS ----------------------------

def take(count, iterable):
    counter = 0
    for item in iterable: # it preservers the status here, and comes back here on next loop (stateful)
        if counter == count:
            return        
        counter += 1
        yield item


def distinct(iterable):
    items = set() # items = list()
    for item in iterable:
        if item in items:
            continue
        yield item
        items.add(item) # items.append(item)


def runPipeline():
    items = [5, 2, 3, 4, 5, 5, 6, 8, 7, 5, 1, 2, 4, 6, 8, 5, 7]
    for item in take(20, distinct(items)):
        print(item)
        

if __name__ == '__main__':
    runPipeline()

