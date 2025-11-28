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




