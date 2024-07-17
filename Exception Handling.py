
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
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")