# Day 2: Basic Calculator in Python

"""
Topic:
Today, I'll build a simple calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
This exercise will help me understand how to handle user inputs, perform calculations, and display results in Python.
"""

# Function to add two numbers
# Hint: You can use the '+' operator to perform addition.
# def add(a, b):
#     # Implement the addition logic here
#     # return a + b

# Function to subtract two numbers
# Hint: You can use the '-' operator to perform subtraction.
# def subtract(a, b):
#     # Implement the subtraction logic here
#     # return a - b

# Function to multiply two numbers
# Hint: You can use the '*' operator to perform multiplication.
# def multiply(a, b):
#     # Implement the multiplication logic here
#     # return a * b

# Function to divide two numbers
# Hint: You can use the '/' operator to perform division. Be careful with division by zero.
# def divide(a, b):
#     # Implement the division logic here
#     # if b != 0:
#     #     return a / b
#     # else:
#     #     return 'Cannot divide by zero'

# Test Cases
# Example 1: Adding 5 and 3 should return 8
# print(add(5, 3)) # Expected output: 8

# Example 2: Subtracting 5 from 3 should return -2
# print(subtract(3, 5)) # Expected output: -2

# Example 3: Multiplying 5 and 3 should return 15
# print(multiply(5, 3)) # Expected output: 15

# Example 4: Dividing 6 by 3 should return 2
# print(divide(6, 3)) # Expected output: 2

# Reference: To learn more about functions and arithmetic operations, visit the Python documentation: https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator


number1 = int(input("Enter your First Number: "))
number2 = int(input("Enter your Second Number: "))

def addNum(a,b):
  c = a + b
  return c

def subNum(a,b):
  c = a - b
  return c

def mulNum(a,b):
  c = a * b
  return c

def divideNum(a,b):
  c = a / b
  return c

print("Addition of two numbers is: ",addNum(number1,number2))

print("Subtraction of two numbers is: ",subNum(number1,number2))

print("Mul of two numbers is: ",subNum(number1,number2))

print("Division of two numbers is: ",divideNum(number1,number2))