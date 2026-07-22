# ============================================
# STRINGS
# ============================================
# Ordered, immutable (cannot be changed once created), indexed by position

text = "Hello Python"

print(text[0])              # indexing -> H
print(text[-1])             # last character -> n
print(text[0:5])            # slicing -> Hello
print(text[::-1])           # reverse the string -> nohtyP olleH

print(text.upper())         # HELLO PYTHON
print(text.lower())         # hello python
print(text.strip())         # removes leading/trailing whitespace
print(text.split(" "))      # splits into a list -> ['Hello', 'Python']
print(text.replace("Python", "World"))
print(len(text))            # length of string
print("Python" in text)     # membership check -> True

# Strings are immutable - this would cause an error:
# text[0] = "J"   # TypeError

name = "John"
age = 25
print(f"{name} is {age} years old")   # f-string formatting


# ============================================
# LIST
# ============================================
# Ordered, mutable (can change), allows duplicates, indexed

fruits = ["apple", "banana", "cherry", "apple"]

print(fruits[0])            # indexing -> apple
print(fruits[-1])           # last item -> apple
print(fruits[1:3])          # slicing -> ['banana', 'cherry']

fruits.append("mango")      # add to end
print(fruits)

fruits.insert(1, "kiwi")    # insert at specific position
print(fruits)

fruits.remove("apple")      # removes FIRST matching value
print(fruits)

fruits.pop()                 # removes last item, returns it
print(fruits)

print(len(fruits))           # length
print("banana" in fruits)    # membership check
fruits.sort()                 # sorts in place
print(fruits)
fruits.reverse()              # reverses in place
print(fruits)

# Lists allow duplicates and are mutable:
fruits[0] = "orange"          # allowed, unlike strings
print(fruits)


# ============================================
# TUPLE
# ============================================
# Ordered, IMMUTABLE (cannot change), allows duplicates, indexed
# Basically a "locked" list - use when data shouldn't change

coordinates = (10, 20, 30)

print(coordinates[0])         # indexing -> 10
print(coordinates[-1])        # last item -> 30
print(coordinates[0:2])       # slicing -> (10, 20)

print(len(coordinates))       # length
print(20 in coordinates)      # membership check

# Tuples are immutable - this would cause an error:
# coordinates[0] = 99   # TypeError

# But you CAN reassign the whole tuple to a new one:
coordinates = (10, 20, 99)
print(coordinates)

# Common real use: returning multiple values from a function,
# or representing fixed data like (latitude, longitude)

single_item_tuple = (5,)      # note the comma - required for single-item tuples
print(type(single_item_tuple))


# ============================================
# SET
# ============================================
# Unordered, mutable, NO duplicates allowed, NOT indexed

numbers = {1, 2, 3, 3, 4, 4, 5}
print(numbers)                 # duplicates automatically removed -> {1,2,3,4,5}

numbers.add(10)                # add an item
print(numbers)

numbers.remove(3)              # remove an item (errors if not found)
print(numbers)

numbers.discard(100)           # remove if exists, no error if missing
print(numbers)

print(3 in numbers)            # membership check (very fast for sets)
print(len(numbers))            # length

# Set operations - useful for comparing collections
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))              # combines both, no duplicates -> {1,2,3,4,5,6}
print(a.intersection(b))       # common elements -> {3,4}
print(a.difference(b))         # in a but not in b -> {1,2}
print(a.symmetric_difference(b)) # in a or b, but not both -> {1,2,5,6}

# Sets have NO indexing - this would cause an error:
# print(numbers[0])   # TypeError


# ============================================
# DICTIONARY
# ============================================
# Key-value pairs, mutable, unordered (in older Python), 
# keys must be unique

student = {
    "name": "John",
    "age": 21,
    "course": "Computer Science"
}

print(student["name"])          # access by key -> John
print(student.get("age"))       # safer way to access -> 21
print(student.get("grade", "N/A"))  # default if key missing -> N/A

student["age"] = 22             # update a value
print(student)

student["grade"] = "A"          # add a new key-value pair
print(student)

del student["course"]           # remove a key
print(student)

print(student.keys())           # all keys
print(student.values())         # all values
print(student.items())          # all key-value pairs

print("name" in student)        # membership check (checks KEYS)

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")


# ============================================
# QUICK SIDE-BY-SIDE COMPARISON
# ============================================

print("\n--- Comparison ---")
my_list = [1, 2, 2, 3]           # ordered, mutable, duplicates allowed
my_tuple = (1, 2, 2, 3)          # ordered, immutable, duplicates allowed
my_set = {1, 2, 2, 3}            # unordered, mutable, NO duplicates
my_dict = {"a": 1, "b": 2}       # key-value pairs, mutable, unique keys

print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)