## Tuples are inmutable

tuple1 = (1,2,"hello")

print(type(tuple1))

print(tuple1[-1])

tuple1 = tuple1 + ("hard rock", 10)
print(tuple1)

print(tuple1[0:4])

print("len", len(tuple1))

## Para ordenar de menor a mayor
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)
print("RatingsSorted: ",  RatingsSorted)


NestedT = (1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

print(NestedT[2][1])

print(NestedT[-1][1][-2])

print("disco".find('s'))


tuplet5 = (1,2,3,4)
print(len(tuplet5))