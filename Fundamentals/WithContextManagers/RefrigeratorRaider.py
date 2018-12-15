'''Demonstrate raiding a refrigerator'''

from contextlib import closing

class RefrigeratorRaider:

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health warming!")
        print("Taking {}".format(food))

    def close(self):
        print("Close the fridge door")

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        r.close()


raid('deep fried pia')
        

