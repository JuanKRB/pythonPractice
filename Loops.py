
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for color in colors:
    print(color)

# It goes from 1 to 10
for number in range(1, 11):
    print(number)

print("//////")

# It goes from 0 to 10
for number in range(11):
    print(number)

print("//////")

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")

print("///While///")

count = 1
while count <= 7:
    print(count)
    count += 1