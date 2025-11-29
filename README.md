# python-fundamentals
This repository contains my Python learning journey, covering:

Basic programs

Loops

Functions

Lists, Tuples, Dictionaries

File Handling

Exception Handling

Object-Oriented Programming (OOP)

Mini Projects

Calculator

Password Generator

Notes App

I will keep updating this repository regularly as I improve my Python skills.

day 1 complete
Introduction to Python
Q1) What is Python?

Python is a high-level, interpreted programming language. It is used to tell the computer what to do in an easy, human‑like way.

Q2) Why is Python so popular?

Here’s why everyone—from beginners to big tech companies—loves Python:

Easy to learn & read — Code looks like plain English.

Versatile — Used in web development, AI, data science, automation, etc.

Beginner‑friendly — No prior coding experience needed.

Cross‑platform — Works on Windows, Mac, Linux, and even Android.

Huge community — Millions of people use it, so help is always available.

✨Python as Interpreted Language✨

Python is interpreted, not compiled.

Unlike languages like C or Java, Python does not need compilation before running.

You just write → run → see output instantly

Q3) Where is Python used?
Area	Examples
Web Development	Instagram, YouTube (using Python frameworks like Django, Flask)
Artificial Intelligence (AI)	ChatGPT, Alexa, self‑driving cars
Data Science	Analyzing data, making graphs & reports
Automation	Auto-email sending, file renaming, daily tasks scripts
Game Development	Basic 2D/3D games using libraries like Pygame

PYTHON NOTES
1. Operators
Operands & Operator Example
7+4
Operands: 7 and 4

Operator: +

Result: 11

Arithmetic Operators
a = 7
b = 4
c = a + b
print(c) # Output: 11

Variables & Data Types
Variable

A variable is a container (a box) used to store data.

Example:
a = 1
b = 2
name = "vidhi"
print(a + b)
print(name)
Data Types

Data type defines the type of data stored in a variable.

Examples:
a = 1 # integer (int)
b = 5.22 # float
ame = "Vidhi" # string (str)
d = True # boolean
E = None # none type

Rules for Variables

Can contain alphabets, digits, underscore

Must start with alphabet or underscore

Cannot start with digits

No spaces allowed

Operators in Python

Arithmetic operators → + - * / % // **

Assignment operators → = += -= *= /=

Comparison operators → == != > < >= <=

Logical operators → and, or, not

Q5) External Module Installation Example

Example: Installing pyttsx3 module
# go to terminal and install
pip install pyttsx3

''' righnow i did copy this from chatgpt because I want to learn about module later I do ki myself'''

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak fastest")
engine.runAndWait()

Q6) Using OS Module to List Directory Files

import os

# specify directory path
directory_path = "New folder"


# list files and folders
contents = os.listdir(directory_path)


# print all items
for item in contents:
print(item)

Q7) Printing a Poem

print("""
Twinkle Twinkle little star
How I wonder what you are
""")

✨Comments in Python✨

Single line comment → # this is comment

Multi-line comment →"""
this is
multi line comment
"""

✨REPL (Python Interactive Mode)

R = Read E = Eval P = Print L = Loop

Example (in terminal):
>>> 5 * 1
5
>>> 5 * 2
10
>>> 5 * 3
15
...
#DAY 2
Chapter – Strings
What is a string?
It is a datatype.

It is a sequence of characters enclosed in quotes (' ' or " " or """ """).

Strings are immutable.

Ways to create strings
a = 'Vidhi'
b = "Vidhi"
c = """Vidhi"""
String Slicing
Example:

Name = "VIDHI"
Index:   0 1 2 3 4
Index:  -5 -4 -3 -2 -1
Length = 5
Syntax
s1 = name[ind_start : ind_end]
Example
name = "Vidhi"
nikname = name[0:3]   # OR name[:3]
print(nikname)
Slicing with Skip Value
word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word[3:8:2]
Output:

dfh
Use of Comparison Operator
Check whether variable a is greater than b.

a = 34
b = 80
print("a is greater than b or not:", a > b)
Output:

False
Find Average of Two Numbers
a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
print("Average of two numbers is:", (a + b) / 2)
Output Example

Enter number 1: 10
Enter number 2: 10
Average of two numbers is: 10
Find Square of a Number
a = int(input("Enter a number: "))
print("Square of a number is:", a * a)
Output Example

Enter a number: 4
Square of a number is: 16
Practical Set – Chapter 2
Q1 – Add Two Numbers
a = 2
b = 7
print(a + b)
Output:

9
Q2 – Remainder When a Number Is Divided
a = 36
b = 5
print("Remainder when a number is divided by b is:", a % b)
Output:

1
Q3 – Check Type of Variable from input()
a = input("Enter the value of a: ")
print(type(a))
Output:

<class 'str'>
Integer Conversion in input()
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("Number a is:", a)
print("Number b is:", b)
print("Sum is:", a + b)
Output Example

Enter number 1: 8
Enter number 2: 2
Number a is: 8
Number b is: 2
Sum is: 10
Type Conversion (Type Casting)
Convert String to Int
a = "43"
t = type(a)
print(t)
Output:

<class 'str'>
Convert to float:

a = "43"
b = float(a)
t = type(b)
print(t)
Output:

<class 'float'>
input() Function Example
a = input("Enter number 1: ")
b = input("Enter number 2: ")

print("Number a is:", a)
print("Number b is:", b)
print("Sum is:", a + b)
Why does it show 32 instead of 5?
Because input() treats values as string, so "3" + "2" becomes "32" (concatenation).

Logical Operators
OR Truth Table
a	b	a or b
True	True	True
False	False	False
True	False	True
False	True	True
AND Truth Table
a	b	a and b
True	True	True
False	False	False
True	False	False
False	True	False
NOT Example
print(not False)
Type Casting Examples
a = 3
print(type(a))   # int

a = 4.5
print(type(a))   # float

a = "Vidhi"
print(type(a))   # str
Arithmetic Operators
a = 7
b = 4
c = a + b
print(c)
Output:

11
Assignment Operators
a = 4 - 2
print(a)   # 2

b = 6
b += 3
print(b)   # 3 (Notebook has mistake; correct result = 9)
Comparison Operators
d = 5 > 4
print(d)
true




