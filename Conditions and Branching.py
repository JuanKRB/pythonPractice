
# Compare characters

# ASCII
# A: 65
# B: 66
'B' > 'A'

# Compare characters
# When there are multiple letters, the first letter takes precedence in ordering:
'BA' > 'AB'

# The equality operator is case-sensitive
print("Case-sensitive: ", "a" == "A")

age1 = 2

if(age1 == 2):
    print("age1: 2")

if(age1 != 2):
    print("Age's not 2")

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

user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = input("Enter the amount to withdraw: ")
    if amount % 10 == 0:
        print("dispense_cash(amount)")
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")

print("///////////")

# vars can not only be with numbers
# 1=2

friend1_likes_comedy = True
friend2_likes_action = False
friend3_likes_drama = False
if friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:
    print("choose a movie()")


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



