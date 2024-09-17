# Function to add two numbers
def add_numbers(num1, num2):
    """Adds two numbers and returns their sum."""
    return num1 + num2

# Function to check if a number is even
def is_even(number):
    """Checks if a number is even and returns True or False."""
    return number % 2 == 0

# Function to reverse a string
def reverse_string(text):
    """Reverses a string and returns the reversed version."""
    return text[::-1]  # Slicing with a step of -1 reverses the string

# Function to count the number of vowels in a string
def count_vowels(text):
    """Counts the number of vowels in a string and returns the count."""
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

# Function to calculate the factorial of a non-negative integer
def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Function that acts as a decorator (currently does nothing)
def apply_decorator(func):
    """Applies a decorator to a function."""
    return func

# Class representing a Car
class Car:
    """Represents a car with make, model, and year."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Prints the car's information."""
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Function to sort a list of tuples by the second element of each tuple
def sort_by_second(tuples):
    """Sorts a list of tuples by the second element."""
    return sorted(tuples, key=lambda x: x[1])

# Function to merge two dictionaries
def merge_dictionaries(dict1, dict2):
    """Merges two dictionaries and returns the merged dictionary."""
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict

# Examples of usage:

# add_numbers
print("add_numbers(5, 3):", add_numbers(5, 3))  # Output: 8

# is_even
print("is_even(4):", is_even(4))  # Output: True
print("is_even(7):", is_even(7))  # Output: False

# reverse_string
print("reverse_string('hello'):", reverse_string("hello"))  # Output: "olleh"

# count_vowels
print("count_vowels('hello world'):", count_vowels("hello world"))  # Output: 3

# calculate_factorial
print("calculate_factorial(5):", calculate_factorial(5))  # Output: 120

# apply_decorator
@apply_decorator
def example_func():
    return "This function is decorated!"

print("example_func():", example_func())  # Output: "This function is decorated!"

# Car class
my_car = Car("Toyota", "Corolla", 2020)
print("Car information:")
my_car.display_info()

# sort_by_second
tuples = [(1, 3), (2, 2), (3, 1)]
print("sort_by_second(tuples):", sort_by_second(tuples))  # Output: [(3, 1), (2, 2), (1, 3)]

# merge_dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print("merge_dictionaries(dict1, dict2):", merge_dictionaries(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}
