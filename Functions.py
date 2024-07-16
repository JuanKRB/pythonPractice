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