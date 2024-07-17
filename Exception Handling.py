
# result = 10 / 0
# print(result)
# Raises ZeroDivisionError

# print("///////")

# num = int("abc")
# Raises ValueError

# print("///////")

# with open("nonexistent_file.txt", "r") as file:
#        content = file.read()   # Raises FileNotFoundError

# print("///////")

#my_list = [1, 2, 3]
#value = my_list[1] # No IndexError, within range
#missing = my_list[5]  # Raises IndexError

# print("///////")

#my_dict = {"name": "Alice", "age": 30}
#value = my_dict.get("city")  # No KeyError, using .get() method
#missing = my_dict["city"]  # Raises KeyError

# print("///////")

# result = "hello" + 5
# Raises TypeError

# print("///////")

#text = "example"
#length = len(text)  # No AttributeError, correct method usage
#missing = text.some_method()  # Raises AttributeError

# print("///////")

# using Try- except
"""try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")
"""

# 1/0
# y = a + 5
"""a = [1, 2, 3]
a[10]"""

"""""
a = 1

try:
    b = int(input("Please enter a number to divide a: "))
    a = a / b
    print("Success a=", a)
except:
    print("There was an error")

"""
"""""
try:
    b = int(input("Please enter a number to divide a: "))
    a = a / b
    print("Success a=", a)
except (ZeroDivisionError, NameError):
    print("ZeroDivisionError or NameError")
"""""
"""""
try:

except ZeroDivisionError:

except NameError:
"""""

# potential code before try catch
"""""
a = 1

try:
    b = int(input("Please enter a number to divide a: "))
    a = a / b
    print("Success a=", a)
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("NameError")
except:
    print("another exception")
"""""
# code that will execute if there is no exception or a one that we are handling

"""""
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a / b
    print("Success a=", a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
"""""

# potential code before try catch
"""""
try:
# code to try to execute
except ZeroDivisionError:
# code to execute if there is a ZeroDivisionError
except NameError:
# code to execute if there is a NameError
except:
# code to execute if ther is any exception
else:
# code to execute if there is no exception

"""""

"""""
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
"""""

# Practice

"""""
def safeDivide(numerator, denominator):
    try:
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("Error, Cannot divide by 0")

numerator = int(input("Input the numerator: "))
denominator = int(input("Input the denominator: "))

safeDivide(numerator,denominator)
"""""

"""""
import math

def squareRoot(number):
    try:
        squareRoot = math.sqrt(number)
        print("Square root: ", squareRoot)
    except ValueError:
        print("Please, input a positive integer or a float value")

number = int(input("Input the number: "))

squareRoot(number)

"""""

# it shows error when I use 5
def complex_calculation(num):
    try:
        result = num / (num - 5)
        print (f"Result: {result}")
    except Exception as e:
        print(f"An error occurred during calculation. {e}")

user_input = float(input("Enter a number: "))
complex_calculation(user_input)