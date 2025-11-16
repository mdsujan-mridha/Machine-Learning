#check IDE
print('Hello Python!')

# declare variable in python 
x = 10
y = 20
print(x + y)

x="Hello"
y=" Python"
print(x + y)
# Data Types in Python 
a = 10          # Integer
b = 10.5        # Float
c = "Hello"     # String
d = True        # Boolean
e = [1, 2, 3]   # List
f = (1, 2, 3)   # Tuple
g = {1, 2, 3}   # Set
h = {'name': 'John', 'age': 30}  # Dictionary
print(type(a))
print(type(b))  
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

# Type Conversion in Python
x = 10        # int
y = 10.5      # float
z = "20"      # str

# int to float
a = float(x)
print(a)  # 10.0
# float to int
b = int(y)
print(b)  # 10
# str to int
c = int(z)
print(c)  # 20
# str to float
d = float(z)
print(d)  # 20.0
# int to str
e = str(x)
print(e)  # "10"
# float to str
f = str(y)
print(f)  # "10.5"
# Input and Output in Python

user_int1 = int(input("Enter first integer: "))
user_int2 = int(input("Enter second integer: "))

print("You entered:", user_int1, "and", user_int2)
print("Sum:", user_int1 + user_int2)

# String slicing & formatting
my_string = "Hello, Python World!"
print(my_string[0:5])  # Hello
print(my_string[7:13]) # Python
print(my_string[-6:])   # World!
formatted_string = "My name is {} and I am {} years old.".format("Alice", 25)
print(formatted_string)
f"Formatted string: My name is {'Bob'} and I am {30} years old."
