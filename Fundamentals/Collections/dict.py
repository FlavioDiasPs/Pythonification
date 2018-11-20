
#BASICS
dictorary = {"google": "chrome",
             "microsoft":"edge",
             "apple":"saphari",}
dictorary
dictorary["apple"]

#COPING AND UPDATING
d = dict(um=1, dois=2, tres=3, quatro=4)
d
d['um']
e = d.copy()
f = dict(e)
g = dict(cinco=5, seis=6)
f.update(g)
f.update(dict(sete=7, oito=8))
f

#ITERATION
def keyLoop():
    f = dict(um=1, dois=2, tres=3, quatro=4)
    for key in f:
        print("key: {}, value: {}".format(key, f[key]))
keyLoop()

def valueLoop():
    f = dict(um=1, dois=2, tres=3, quatro=4)
    for value in f.values():
        print(value)
valueLoop()

def loopDictAsTuple():
    f = dict(um=1, dois=2, tres=3, quatro=4)
    for key, value in f.items():
        print("key: {}, value: {}".format(key, value))
loopDictAsTuple()

# Pretty Printing
from pprint import pprint as pp
pp(f)