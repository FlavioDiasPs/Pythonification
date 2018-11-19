
s="show how to index into sequences".split()
print(s)

#dealing with negative indexes
print(s[5])
print(s[-5]) #accepts negative index, always starting the counting over the index 0

#list slicing
s="show how to index into sequences".split()
s[1:3]
s[3:]

#copy the list
full_slice = s[:] # or s.copy(), or list(s)
full_slice is s # this is a new list
full_slice == s # however they have the same content

# does not copy the list
full_slice = s
full_slice is s # this is the same list

#INNER LISTS
#THE COPY OCCURS ONLY AT THE TOP LEVEL, THE BOTTOM LEVEL ARE STILL THE SAME IN MEMORY REFERENCE
#IS IS CALLED SHALLOW COPIES, SO CHANGING INDEX 2, ACTUALLY CHANGES ALL INDEXES
s = [[-1, 1]] * 5
s[2].append(7)
s

#CHECK ON THE LIST
u = "flavio tem muito o que estudar ainda".split()
u
u.index("muito") #gives the index
u[4]
"tem" in u #gives a bool
"tasaem" in u #gives a bool

#INSERT, REMOVE AND JOIN
u = "flavio tem muito o que estudar ainda".split()
del u[2]
u.remove("tem")
u.insert(1, "tem")
u.append("krl")
u
s = " ".join(u)
s

#CONCATENATE LISTS, NO MATTER DE TYPE
a = [4, 5, 6]
b = [1, 2, 3]
c = a + b
c
c.extend(["a", "b", "c"])
c

#REVERSE AND SORT LIST
a = [4, 5, 6]
b = [1, 2, 3] 
c = a + b
c
c.reverse()
c
c.sort()
c
c.sort(reverse = True)
c

#ADVANCED SORTING
a = "Flavio ainda tem muito o que estudar".split()
a.sort(key=len)
a

a = "Flavio ainda tem muito o que estudar".split()
b = sorted(a)
c = reversed(a)
a # not altered
b # sorted
c # iterator object
