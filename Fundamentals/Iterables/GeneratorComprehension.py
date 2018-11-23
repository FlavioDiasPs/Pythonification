
squares = (x*x for x in range(100))
# print(next(squares))

for gen in squares:
    if gen > 500:
        break
    print(gen)



sum(x*x for x in range(100))