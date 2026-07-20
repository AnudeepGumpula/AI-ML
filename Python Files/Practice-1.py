# VARIABLES & DATA TYPES

name = "John"
age = 25
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# Check data type of a variable
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# BASIC INPUT/OUTPUT

# print with multiple values
print("Name:", name, "Age:", age)

# f-strings (formatted output, very commonly used)
print(f"My name is {name} and I am {age} years old")

# taking input from user (input always returns a string)
user_name = input("Enter your name: ")
print("Hello,", user_name)

# TYPE CASTING / CONVERSION

num_str = "10"
num_int = int(num_str)
print(num_int + 5)

price = "99.99"
price_float = float(price)
print(price_float)

age_num = 25
age_str = str(age_num)
print("I am " + age_str + " years old")



# OPERATORS

# Arithmetic
a = 10
b = 3
print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division (returns float)
print(a // b)  # floor division
print(a % b)   # modulus (remainder)
print(a ** b)  # exponent (power)


# Comparison operators
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# Logical operators
x = True
y = False
print(x and y)
print(x or y)
print(not x)


# STRINGS BASICS


text = "Hello World"
print(len(text))          # length of string
print(text.upper())       # uppercase
print(text.lower())       # lowercase
print(text[0])             # first character
print(text[-1])            # last character
print(text[0:5])           # slicing
print(text.replace("World", "Python"))



# BRANCHING STATEMENTS (if-else)


# Basic if
age = 20
if age >= 18:
    print("You are an adult")


# if-else
marks = 40
if marks >= 50:
    print("Pass")
else:
    print("Fail")


# if-elif-else
score = 75
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")


# Nested if
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")


# Multiple conditions with and/or
temperature = 30
is_raining = False

if temperature > 25 and not is_raining:
    print("Good day for a walk")
else:
    print("Maybe stay inside")


# Ternary (short-hand if-else)
num = 10
result = "Even" if num % 2 == 0 else "Odd"
print(result)


# Checking membership with if (using 'in')
fruits = ["apple", "banana", "cherry"]
check = "banana"
if check in fruits:
    print(f"{check} is in the list")
else:
    print(f"{check} is not in the list")