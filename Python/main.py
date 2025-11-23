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
# formatting string 
formatted_string = "My name is {} and I am {} years old.".format("Alice", 25)
print(formatted_string)
f"Formatted string: My name is {'Bob'} and I am {30} years old." 

# list, list methods 
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list);
my_list.remove(3)
print(my_list);
my_list.pop()
print(my_list);
my_list.sort(reverse=True)
print(my_list);
my_list.insert(2, 10)
print(my_list);
my_list.reverse()
print(my_list);
print("Length of list:", len(my_list));
print("Index of 10:", my_list.index(10));
print("Count of 2:", my_list.count(2));
my_list.extend([7, 8, 9])
print(my_list);

# tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print("Length of tuple:", len(my_tuple))
print("Index of 3:", my_tuple.index(3))
print("Count of 2:", my_tuple.count(2))

print("length of 5:",my_tuple.count(5));

# sets 
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print("My sets",my_set)
my_set.remove(3)
print(my_set)
my_set.discard(10)  # does not raise error if element not found
print(my_set)
my_set.pop()
print(my_set)
print("Length of set:", len(my_set))
print("Is 4 in set?", 4 in my_set)
my_set2 = {4, 5, 6, 7, 8}
union_set = my_set.union(my_set2)
print("Union:", union_set)
intersection_set = my_set.intersection(my_set2)
print("Intersection:", intersection_set)
difference_set = my_set.difference(my_set2)
print("Difference:", difference_set)
symmetric_difference_set = my_set.symmetric_difference(my_set2)
print("Symmetric Difference:", symmetric_difference_set)


# dictionaries 
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print("My new dictionaries: ",my_dict)

print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
print("My name: ",my_dict['name']);
my_dict['age'] = 31
print("Updated age:", my_dict['age'])

# take a new dictionary 
student = {
    "id": 101,
    "name": "Bob",
    "courses": ["Math", "Science"]
}
print("Taken courses:",student["courses"][1]);
# replace course 
student["courses"]= "Physics"
print("Taken courses:",student["courses"]);
student["courses"]= ["Math", "Science", "Physics"]
print("Updated courses:",student["courses"]);


# conditions 
a = 10
b = 20
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")


# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit":
    print("Looking around in the kitchen.")
elif room == "bed":
    print("Looking around in the bedroom.")
else:
    print("Looking around elsewhere.")

# if-elif-else construct for area
if area > 15:
    print("Big place!")
else:
    print("Pretty small.")

# Looking around in the bedroom. 
# Pretty small.
# nested conditions 
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
 
# loops 
for i in range(5):
    print("For loop iteration:", i) 
    
# take a set of numbers and print even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print("Even number:", num)
            
        
# take a empty set and where append number 1 to 10 
even_numbers = []
for num in range(1, 11):
        even_numbers.append(num)
        print("Current even numbers list:", even_numbers)    
        
# while loop 
count = 0
while count < 5:
    print("While loop count:", count)
    count += 1
 
 
# take a set of numbder
numbers= [];
i=1;
while i <=10:
    numbers.append(i);
    i +=1;
    print("Current numbers list:", numbers);   
  
# brek and continue
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("Current i value:", i)
for i in range(10):
    if i % 2 == 0:
        print("Skipping even number i =", i)
        continue
    print("Current odd i value:", i)
  
      