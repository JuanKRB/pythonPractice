colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for color in colors:
    print(color)

print("//////")

dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])

print("//////")

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

print("//////")

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

print("///While///")

count = 1
while count <= 7:
    print(count)
    count += 1

print("//////")

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while (year != 1973):
    print(year)
    i = i + 1
    year = dates[i]


print("It took ", i, "repetitions to get out of loop.")

print("//Practice///")

for numberIt in range(-5,6):
    print(numberIt)

print("//////")

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for genre in Genres:
    print(genre)

print("//////")

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

i = 0
rating = PlayListRatings[0]

while(rating > 5):
    print(rating)
    i += 1
    rating = PlayListRatings[i]


print("//////")

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

i = 0

while(squares[i] == 'orange'):
    print(squares[i])
    new_squares.append(squares[i])
    i += 1

print("New squares: ", new_squares)


print("//////")

for i in range(10):
   print("6", " * ", i , " = " , 6 * i)

print("//////")
for i in range(10):
   print("7", " * ", i , " = " , 7 * i)

print("//////")

Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]

Animals7letters = []

for animal in Animals:
    if(len(animal) == 7):
        Animals7letters.append(animal)

print(Animals7letters)

print("//////")

for x in ['A', 'B', 'C']:
    print(x + 'A')

