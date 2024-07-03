# No duplicates elements
"""
aaaa
"""


set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)


album_list = [ "Michael Jackson", "Michael Jackson", "Thriller", 1982, "00:42:19", \
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

print(album_set1.intersection(album_set2) )

# All The values of both of them
print(album_set1.union(album_set2) )