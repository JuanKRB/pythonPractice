def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b

result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12


string_length = len("Hello, World!")
list_length = len([1, 2, 3, 4, 5])

print(string_length)
print(list_length)

print("///////")
total = sum([10, 20, 30, 40, 50])

print(total)

print("///////")
highest = max([5, 12, 8, 23, 16])

print(highest)


print("///////")
lowest = min([5, 12, 8, 23, 16])

print(lowest)

print("///////")

# If I need a function that does nothing
def function_name():
    pass

print("///////")

def greet(name):
    print("Hello, " + name)

result = greet("Alice")
print(result)  # Output: Hello, Alice

print("///////")

def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)

# Show what I have with """ in the function
help(multiply)

print("///////")
def add(a, b):
    return a + b
sum_result = add(3, 5)

print("///////")

global_variable = "I'm global"

def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

print("///////")

def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)
print_numbers(5)

print("///////")

def greet(name):
    return "Hello, " + name
# _ When you're not gonna use the index
for _ in range(3):
    print(greet("Alice"))

print("///////")
my_list = []

# Function to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)


# Function to remove an element from the list
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)

print("Current list:", my_list)

remove_element(my_list, 17)
remove_element(my_list, 55)

print("Updated list:", my_list)

print("///////")
def Mult(a, b):
    c = a * b
    return (c)
    print('This is not printed')

result = Mult(12, 2)
print(result)

result2 = Mult(3, "Michael Jackson ")
print(result2)

print("///////")

def MJ():
    print('Michael Jackson')

def MJ1():
    print('Michael Jackson')
    return (None)

print(MJ())
print(MJ1())

print("///////")
def con(a, b):
    return(a + b)

print(con("This ", "is"))

print("///////")
def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"

x = type_of_album("Michael Jackson", "Thriller", 1981)
print(x)

print("///////")

def PrintList(the_list):
    for element in the_list:
        print(element)


PrintList(["hi", 2.5, "bye"])

def PrintList(the_dic):
    for value in the_dic.values():
        print(value)

PrintList({"key1":2, "key": 4.5})

# Compare Two Strings Directly using in operator
# add string
string = "Michael Jackson is the best"


print("///////")
def check_string(text):
    # Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'


print(check_string("Michael Jackson is th"))


print("///////")


# Compare two strings using == operator and function
def compareStrings(x, y):
    # Use if else statement to compare x and y
    if x == y:
        return 1

# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

# Use if else statement to compare the string
if check == 1:
    print("\nString Matched")
else:
    print("\nString not Matched")

print("///////")

# Python Program to Count words in a String using Dictionary
def freq(string):
    # step1: A list variable is declared and initialized to an empty list.
    words = []

    # step2: Break the string into list of words
    words = string.split()  # or string.lower().split()

    # step3: Declare a dictionary
    Dict = {}

    # step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)

    # step5: Print the dictionary
    print("The Frequency of words is:", Dict)


# step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

print("///////")

# Example for setting param with default value
def isGoodRating(rating=4):
    if (rating < 7):
        print("this album sucks it's rating is", rating)

    else:
        print("this album is good its rating is", rating)

isGoodRating()
isGoodRating(10)

print("///////")

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

print("///////")

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

print("///////")
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada', Province='Ontario', City='Toronto')


print("///////")
def addItems(list):
    list.append(("Three", "hi"))
    list.append("Four")


myList = ["One", "Two"]

addItems(myList)

print(myList)


# Quiz on Functions

def div(number1, number2):
    result = number1 / number2
    return result

print(div(8.3, 4.8))

def div2(number1, number2):
    return (number1 / number2)

print("///////")

def con(a, b):
    return(a + b)

print(con(2, 2))

print(con(['a', 1], ['b', 1]))

print("///////")


def findLen(string):
    print(len(string))

little = ("Mary had a little lamb Little lamb,"
          " little lamb Mary had a little lamb"
          ".Its fleece was white as snow And "
          "everywhere that Mary went Mary went,"
          " Mary went Everywhere that Mary went"
          " The lamb was sure to go")

findLen(little)

print("///////")

def freq(string, passedkey):
    # step1: A list variable is declared and initialized to an empty list.
    words = []

    # step2: Break the string into list of words
    words = string.split()  # or string.lower().split()

    # step3: Declare a dictionary
    Dict = {}

    # step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if (key == passedkey):
            Dict[key] = words.count(key)
            # step5: Print the dictionary
    print("Total Count:", Dict)


# step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go", "little")

print(len([sum([1, 1, 1])]))

print("///////")
# The sorted function will not make any changes to the original list.

L=[1,3,2]

sorted(L)

