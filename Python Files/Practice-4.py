"""
==================================================================
Python Notes - Functions, Packages, Map/Filter/Reduce/Iterator/Lambda
==================================================================
"""

# ============================================
# 1. FUNCTIONS - BASICS
# ============================================

def greet():
    print("Hello!")

greet()
greet()   # can call as many times as needed


# Functions with parameters
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("John")
greet_name("Mary")


# Functions with return values
def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # 8


# print() vs return - important distinction
def add_print(a, b):
    print(a + b)   # just displays, gives back None

def add_return(a, b):
    return a + b    # actually hands back a usable value

x = add_print(5, 3)     # prints 8, but x is None
y = add_return(5, 3)    # nothing printed, but y = 8
print(x)   # None
print(y)   # 8


# ============================================
# 2. FUNCTIONS - DEFAULT & KEYWORD ARGUMENTS
# ============================================

def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default()          # Hello, Guest!
greet_default("John")    # Hello, John!


# Keyword arguments - order doesn't matter when named
def student_info(name, age, course):
    print(f"{name}, {age}, {course}")

student_info(name="John", course="CS", age=21)


# ============================================
# 3. *args AND **kwargs
# ============================================

# *args - accepts any number of POSITIONAL arguments (bundled as a tuple)
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))          # 6
print(add_all(1, 2, 3, 4, 5))    # 15


# **kwargs - accepts any number of KEYWORD arguments (bundled as a dict)
def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="John", age=21, course="CS")


# ============================================
# 4. MULTIPLE RETURN VALUES & SCOPE
# ============================================

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 7, 1, 9, 3])
print(low)     # 1
print(high)    # 9


# Local vs global scope
x = 10   # global

def show_x():
    x = 5   # local - only exists inside this function
    print(x)

show_x()      # 5
print(x)      # 10 - global x untouched


counter = 0

def increment():
    global counter   # explicitly modify the global variable
    counter += 1

increment()
increment()
print(counter)   # 2


# Docstrings - documenting a function
def add_documented(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add_documented.__doc__)


# ============================================
# 5. PACKAGES - IMPORTING
# ============================================

import math

print(math.sqrt(16))     # 4.0
print(math.pi)            # 3.14159...
print(math.floor(4.7))    # 4
print(math.ceil(4.2))     # 5


# Importing with an alias
import numpy as np    # np.array(), np.mean(), etc.
# import pandas as pd


# Importing specific functions only
from math import sqrt, pi
print(sqrt(25))    # 5.0 - no need for math.sqrt() anymore
print(pi)


# Importing everything (generally discouraged - unclear where things come from)
# from math import *


# A few useful built-in packages
import random
print(random.randint(1, 10))           # random integer 1-10
print(random.choice(["a", "b", "c"]))  # random item from a list

import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.strftime("%m-%d-%Y"))

import os
print(os.getcwd())     # current working directory
print(os.listdir())    # files in current directory


# ============================================
# 6. LAMBDA FUNCTIONS
# ============================================

# Lambda = small, anonymous (unnamed) function
# Syntax: lambda arguments: expression   (no "return" needed)

def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(square(5))          # 25
print(square_lambda(5))   # 25

add_lambda = lambda a, b: a + b
print(add_lambda(3, 4))   # 7

is_even = lambda n: n % 2 == 0
print(is_even(10))        # True

# Where lambdas actually get used - as quick inline functions
# passed into other functions (map, filter, sorted, etc.)
students = [("John", 85), ("Mary", 92), ("Alex", 78)]
students.sort(key=lambda student: student[1])   # sort by score
print(students)


# ============================================
# 7. MAP
# ============================================
# Applies a function to EVERY item in an iterable -> transforms each one
# Same number of items in as out

numbers = [1, 2, 3, 4, 5]

def square_fn(x):
    return x ** 2

squared = map(square_fn, numbers)
print(list(squared))    # [1, 4, 9, 16, 25]

# More commonly paired with a lambda
squared_lambda = list(map(lambda n: n ** 2, numbers))
print(squared_lambda)   # [1, 4, 9, 16, 25]

# Equivalent list comprehension (many prefer this for readability)
squared_comp = [n ** 2 for n in numbers]
print(squared_comp)

# map() can work across multiple lists at once
list1 = [1, 2, 3]
list2 = [10, 20, 30]
combined = list(map(lambda a, b: a + b, list1, list2))
print(combined)   # [11, 22, 33]


# ============================================
# 8. FILTER
# ============================================
# Keeps only items where a function returns True
# Fewer (or equal) items out than in - unlike map, which transforms every item

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even_fn(x):
    return x % 2 == 0

evens = filter(is_even_fn, numbers)
print(list(evens))   # [2, 4, 6, 8, 10]

# With a lambda (more common in practice)
evens_lambda = list(filter(lambda n: n % 2 == 0, numbers))
print(evens_lambda)

# Equivalent list comprehension
evens_comp = [n for n in numbers if n % 2 == 0]
print(evens_comp)


# ============================================
# 9. REDUCE
# ============================================
# Collapses an iterable down to a SINGLE value
# NOT built-in - must import from functools

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)
print(total)   # 15
# Step by step: 1+2=3 -> 3+3=6 -> 6+4=10 -> 10+5=15

# Reduce with an initial starting value
total_with_start = reduce(lambda x, y: x + y, numbers, 100)
print(total_with_start)   # 110 (starts at 100 instead of the first item)

# Example: finding max manually (just to understand mechanics -
# in real code just use the built-in max())
values = [3, 7, 2, 9, 4]
maximum = reduce(lambda x, y: x if x > y else y, values)
print(maximum)   # 9


# ============================================
# 10. ITERATOR
# ============================================
# An object that lets you step through a collection ONE ITEM AT A TIME,
# remembering its position. This is what powers every "for" loop internally.

# ITERABLE = something you CAN loop over (list, tuple, string, dict, etc.)
# ITERATOR = the object that actually DOES the looping, from iter()

nums_list = [1, 2, 3]        # this is an ITERABLE
my_iterator = iter(nums_list)  # convert to an ITERATOR

print(next(my_iterator))   # 1
print(next(my_iterator))   # 2
print(next(my_iterator))   # 3
# next(my_iterator))       # would raise StopIteration - no items left

# What a "for" loop is actually doing behind the scenes:
nums_list2 = [1, 2, 3]
for num in nums_list2:
    print(num)

# Equivalent manual version:
iterator2 = iter(nums_list2)
while True:
    try:
        num = next(iterator2)
        print(num)
    except StopIteration:
        break

# Why iterators matter: they allow processing large datasets
# WITHOUT loading everything into memory at once - since each item
# is produced only when asked for. This is the same idea behind generators.


# ============================================
# 11. CHAINING IT ALL TOGETHER
# ============================================
# A common functional-programming style: filter -> map -> reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens_final = filter(lambda x: x % 2 == 0, numbers)         # keep evens
squared_evens = map(lambda x: x ** 2, evens_final)           # square them
total_final = reduce(lambda x, y: x + y, squared_evens)      # sum it all

print(total_final)   # 220  (4 + 16 + 36 + 64 + 100)
