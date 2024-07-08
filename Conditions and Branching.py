
# Compare characters

# ASCII
# A: 65
# B: 66
'B' > 'A'

# Compare characters
# When there are multiple letters, the first letter takes precedence in ordering:
'BA' > 'AB'

## Branching

age = 19

if age > 18:
    print("You're greater than 18")
elif age == 18:
    print("You're 18")
else:
    print("You're under 18")

print("You can move on")

print("///////////")

albumYear = 1980

if(albumYear > 1979) and (albumYear < 1990):
    print("albumYear is between 1980 and 1989")

print("You're out of there")

print("///////////")

albumYear2 = 1990

if(albumYear2 < 1980) or (albumYear2 > 1989):
    print("albumYear wasn't made in the 80's")
else:
    print("it was indeed made in the 80's")

print("You're out of there2")

albumYear3 = 1983

print("///////////")

if not(albumYear3 == 1984):
    print("It's not 1984")

print("///////////")


# Practice
BackInBack = 8.5

if(BackInBack > 8):
    print("The album is amazing")
else:
    print("This album is ok")

print("///////////")

albumYear = 1974

if(albumYear < 1980) or (albumYear == 1991) or (albumYear == 1993):
    print("This album came out in year: ", albumYear)

