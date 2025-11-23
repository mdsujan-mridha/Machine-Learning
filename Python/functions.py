# define a funtion with function name
def greet():
    print("Hello, World!")
# call the function    
greet()

# calculate the sum of two numbers
def sum(a,b):
    return a + b


# take input from user and call the sum function
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = sum(a, b);
print("Sum:", result);

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")     

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil") 

# check oven and odd number 
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number: "))
result = check_even_odd(number)
print(f"The number {number} is {result}.")    

# Positional Arguments

def nameAge(name,age):
    print("Hi, i am", name)
    print("My age is", age)
    
print("Case-1:")
nameAge("Alice", 30)
print("Case-2:")
nameAge(age=25, name="Bob")    


# Arbitrary Arguments
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')

# Anonymous Functions

def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))   

# Pass by Reference and Pass by Value
def myFun(x):
    print("Inside Function:", x)
    x[0] = 20
    
    
 
list = [10,11,12,13]

myFun(list)

print(list)    


# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified

# function that sort number of array 
def sort_numbers(num_list):
    num_list.sort()
    return num_list
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_numbers(numbers)
print("Sorted Numbers:", sorted_numbers)
print("Original Numbers:", numbers)  # original list is modified

# sorting descinding order 
def sort_numbers_desc(num_list):
    num_list.sort(reverse=True)
    return num_list
numbers_desc = [3, 8, 1, 4, 7]
sorted_numbers_desc = sort_numbers_desc(numbers_desc)
print("Sorted Numbers (Desc):", sorted_numbers_desc)
print("Original Numbers (Desc):", numbers_desc)  # original list is modified
