# No duplicates elements
# Can't have others in it
# But tuplets can because they can't change  (siempre y cuando todos sus elementos sean hashables)
"""
aaaa
"""


set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)


album_list = [ "Michael Jackson", "Michael Jackson", "Thriller", 1982, "00:42:19",
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)

# -------------------------------------------------------

A = set(["Thriller", "Back in Black", "AC/DC"])

A.add("NSYNC")

A.add("NSYNC")

print(A)

A.remove("NSYNC")

print(A)

print("AC/DC" in A)

# -------------------------------------------------------

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

print(album_set1, album_set2)

# The values which the two of them have
intersection = album_set1 & album_set2
print(intersection)

# The values which are ONLY in album_set2
print(album_set1.difference(album_set2))

# The values which are ONLY in album_set1
print(album_set2.difference(album_set1))

print(album_set1.intersection(album_set2))

# All The values of both of them
print(album_set1.union(album_set2))



album_setEJ1 = set(['AC/DC', 'Back in Black'])
album_setEJ2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

## Revisa si todo lo de album_setEJ2 esta en el
print(album_setEJ2.issuperset(album_setEJ1))

## Revisa si todo esta en album_setEJ2
print(set({"Back in Black", "AC/DC"}).issubset(album_setEJ2))


"""
Quiz on Sets
"""

set(['rap','house','electronic music', 'rap'])


# La suma da diferente xq el set elimina los duplicados
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))




album_set12 = set(['AC/DC', 'Back in Black'])
album_set22 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

print(album_set12.union(album_set22))

print(album_set12.issubset(album_set22))

V = {'A', 'B'}
V.add('C')

print(V)

# To delete
V.discard("apple")

# Remove the last one and returns it
removed_fruit = V.pop()
print(removed_fruit)

# To delete, Raises a `KeyError` if the element is not found.
# V.remove("banana")


"""
combined = fruits.union(colors) 
common = fruits.intersection(colors) 
unique_to_fruits = fruits.difference(colors) 
sym_diff = fruits.symmetric_difference(colors)
"""

V.update(["kiwi", "grape"])

V.update(["kiwi3", "grape6"])

print(V)