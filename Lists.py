list2 = [2,3,"Hi"]

print(list2[-1])

print(list2[0:2])

a = [1, 'a']

b = [2, 1, 'd']

a.append(b)

print(a)

b.extend(a)

print(b)

print(len(b))

print(b[-6])

del(b[-1])

print(b)

print(type(b))

old_list = [1, 2, 3, 4, 5]
new_list = old_list[:]

print(new_list)

