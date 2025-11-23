# What is Module in Python?

# The module is a simple Python file that contains collections of functions and global variables and with having a .py extension file. It is an executable file and to organize all the modules we have the concept called Package in Python. 

# def myModule(name):
#     print("This is My Module : "+ name)
# import demo_module
# demo_module.myModule("Math")

from datetime import date
d= date.today()
print("Today's Date is : ",d)

# random function 
from random import random as rd 
print("Random Number is : ",rd())

# What is Package in Python?

# The package is a simple directory having collections of modules. This directory contains Python modules and also having __init__.py file by which the interpreter interprets it as a Package. The package is simply a namespace. The package also contains sub-packages inside it.     


# numpy 
#!H:\Project\Machine Learning\myenv\Scripts\pip.exe
import numpy as np
x = np.array([1,2,3])

print("Numpy Array is : ",x)

# 2D array 
y= np.array([[1,2,3],[4,5,6]])
print("2D Numpy Array is : \n",y)

# 3D array
z= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D Numpy Array is : \n",z)

# NumPy basic Operations 
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Addition
add = x + y  
print("Addition:",add)

# Subtraction
subtract = x - y 
print("substration:",subtract)

# Multiplication
multiply = x * y 
print("multiplication:",multiply)

# Division
divide = x / y  
print("division:", divide)