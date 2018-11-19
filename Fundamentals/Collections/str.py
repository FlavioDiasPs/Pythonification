"""Um pouquinho sobre tupla

Usage:
    Selecione a shift + enter
"""

len("fhsryky jsf jasf jsa j js j")

#JOIN AND SPLIT
"Flavio" + "Dias" + "Pegas" #this is a bad way of how to do this, can harm memory and allocations
" ".join(["flavio", "Dias", "Pegas"]) #better way for python
"flavio dias pegas da silva".split(" ")

#PARTITION
"unforgetable".partition("forget") #partitionates the string using the argument as splitter
departure, _, arrival = "São Paulo:Rio de janeiro".partition(':') #_ is used, so partition doenst put useless value into a variable
print(departure)
print(arrival)

#FORMAT 
"This is the {0} format".format("normal")
"This is the format {} the {}".format("omiting", "value")
"This is the {var} way of {use} the format".format(var="variable", use="using")

pos = ("tuple", "using", "thing")
"This is the {pos[0]} way of {pos[1]} this format {pos[2]}".format(pos=pos)

"Math constants: pi={m.pi:.8f}, e={m.e:.3f}".format(m=math) # from module Math