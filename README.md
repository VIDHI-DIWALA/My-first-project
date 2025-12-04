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
#day 3 of learning python
📘 Day 3 – Python Notes (Strings, Lists & Tuples)
-----------------------------------
⭐ Advanced String Slicing
word = "animals"

word[1:6]      # aimals
word[:6]       # animal
word[0:]       # animals
word[0:7]      # animals
⭐ String Functions
1. Find Length
word = "Pen"
print(len(word))
# Output: 3
2. endswith()
word = "Pen"
print(word.endswith("n"))
# Output: True
3. startswith()
Same as endswith(), but checks beginning of the string.

4. capitalize()
name = "vidhi"
print(name.capitalize())
# Output: Vidhi
5. count()
"App".count("p")
# Output: 2
6. find()
word = "Python"
word.find("hon")     # returns position
7. replace()
word = "I love Python"
word.replace("Python", "Java")
8. Other string methods
upper()

lower()

title()

etc.

-----------------------------------
⭐ Escape Sequence Characters
1. \n → New Line
a = "My name is Vidhi \n I am doing BCA"
print(a)
Output:

My name is Vidhi
I am doing BCA
2. \t → Tab Space
a = "My name is Vidhi \t I am doing BCA"
print(a)
3. \" → Double Quotes Inside String
a = "My name is \"Vidhi\""
print(a)
Output:

My name is "Vidhi"
-----------------------------------
⭐ Practice Set – Strings
Q1. Program to display entered name with Good Afternoon
name = input("Your name: ")
print("Good Afternoon, " + name)
Q2. Fill a letter template
Template:

Dear <|name|>,
You are selected!
<|date|>
Code:

letter = """Dear <|name|>,
You are selected!
<|date|>"""

print(letter.replace("<|name|>", "Vidhi").replace("<|date|>", "30 Nov, 2025"))
Q3. Detect double spaces
sentence = "I am  19 years old"
print(sentence.find("  "))
# Output: 3
Q4. Replace double spaces with single space
sentence = "I am  19 years old"
print(sentence.replace("  ", " "))
Q5. Format letter using escape sequences
letter = "Dear Vidhi,\n\tYou are doing great in Python.\nLove you!"
print(letter)
-----------------------------------
⭐ Lists and Tuples (Chapter 4)
Lists
Used to store multiple values.

Mutable (can be changed).

Example
friends = ["Apple", "Orange", 5, 24.6, True, "Sneha"]

print(friends[0])   # Apple
friends[0] = "Banana"
print(friends[0])   # Banana
List Methods
friends = ["Apple", "Orange", 5, 24.6, True]

friends.append("Vidhi")
print(friends)
Other Methods
sort()

reverse()

insert(position, value)

pop(position)

etc.

-----------------------------------
⭐ Tuples in Python
Tuples are immutable (cannot be changed).

a = (1, 45, 342, 2424, False, "Rohini", "Shivam")
print(type(a))
Tuple Methods
1. count()
a = (1, 45, 45, 7)
print(a.count(45))
# Output: 2
2. index()
a = (1, 45, 3424)
print(a.index(3424))
# Output: 2
-----------------------------------
⭐ Practice Set – Lists & Tuples
Q1. Store 3 fruits entered by user
fruits = []

f1 = input("Enter fruit name: ")
fruits.append(f1)

f2 = input("Enter fruit name: ")
fruits.append(f2)

f3 = input("Enter fruit name: ")
fruits.append(f3)

print(fruits)
Q2. Enter marks of 3 students & sort
marks = []

m1 = int(input("Enter marks: "))
marks.append(m1)

m2 = int(input("Enter marks: "))
marks.append(m2)

m3 = int(input("Enter marks: "))
marks.append(m3)

marks.sort()
print(marks)
Q3. Show that tuples cannot be changed
a = (34, 234, "Harry")
a[2] = "Larry"     # ERROR: tuple cannot be changed
Q4. Sum a list with 4 numbers
a = [2, 8, 1, 3]
print(sum(a))      # Output: 14
Q5. Count the number of zeros in tuple
a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)           # Output: 3
#day 4 of learning python
Chapter 5 – Dictionary & Sets
Sets
Definition
A set is a collection of well-defined objects.

Examples
S = {1, 5, 32}        # This is a set
S = set()            # This is how an empty set is made
S = {1, 5, 32, 5, 5}  # Duplicate values are removed
print(S)             # Output: {1, 5, 32}
Set Methods
S = {1, 5, 32, 54, 5, 5, 5, "Harry"}

S.add(566)
print(S)
# Output: {32, 1, 5, 54, 566, "Harry"}
Properties of Set
Sets are unordered

Sets are unindexed

Cannot contain duplicate values

Cannot change individual items (no indexing)

Set Operations
Example:
S = {4, 3, 1, 83}

len(S)          # length of set
S.remove(1)     # removes value 1 → {4, 3, 83}
S.pop()         # removes a random value
S.clear()       # empties the set
Union / Intersection
S1 = {2, 4, 5, 6, 7}
S2 = {7, 8, 1, 9, 83}

print(S1.union(S2))
# Output: {1, 2, 4, 5, 6, 7, 8, 9, 83}

print(S1.intersection(S2))
# Output: {7}
Practice Questions (Sets)
Q1 – Input numbers and display unique values
S = set()

n = int(input("Enter a number: "))
S.add(n)

n = int(input("Enter a number: "))
S.add(n)

n = int(input("Enter a number: "))
S.add(n)

print(S)
Q2 – Can a set contain 18 (int) and "18" (str)?
S = set()
S.add(18)
S.add("18")
print(S)
# Output: {18, "18"}
Q3 – Length of the set
S = set()
S.add(20)
S.add(20.0)
S.add("20")

print(len(S))
# Output: 2
Reason:

20 (int) and 20.0 (float) are considered equal

"20" is a string 
#ANOTHER DAY OF LEARNING PYTHON
## 🔁 Loop Control Statements
### 🔹 Break Statement
for i in range(100):
    if i == 34:
        break
    print(i)
📌 break stops the loop immediately.

### 🔹 Continue Statement
for i in range(100):
    if i == 34:
        continue
    print(i)
📌 continue skips the current iteration.

### 🔹 Pass Statement
for i in range(100):
    pass
i = 0
while i < 45:
    print(i)
    i += 1
📌 pass means “do nothing” (placeholder).

# 🔄 Loops in Python
## ➡️ For Loop Through a List
l = [1, 4, 6, 346, 6, 764]

for i in l:
    print(i)
## ➡️ For Loop Through a Tuple
t = (6, 231, 95, 122)

for i in t:
    print(i)
## ➡️ For Loop Through a String
s = "Vidhi"

for ch in s:
    print(ch)
## ➡️ For Loop with Else
l = [1, 7, 8]

for item in l:
    print(item)
else:
    print("done")
# 🔁 While Loop
i = 1

while i <= 6:
    print(i)
    i += 1
## ➡️ While Loop Through a List
l = ["Harsh", "Vidhi", "Rehana", 1, False]

i = 0
while i < len(l):
    print(l[i])
    i += 1
# 📝 Practice Questions
## Q1️⃣ Username Should Contain At Least 10 Characters
username = input("Enter your username: ")

if len(username) < 10:
    print("Username is less than 10 characters")
else:
    print("OK")
## Q2️⃣ Check if Name Exists in a List
l = ["Vidhi", "Vinita", "Krishita"]

name = input("Enter your name: ")

if name in l:
    print("Your name is in the list")
else:
    print("Your name is not in the list")
## Q3️⃣ Pass or Fail (40% overall + 33 marks each subject)
marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

total_percentage = (marks1 + marks2 + marks3) / 3

if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("You passed")
else:
    print("You failed")
## Q4️⃣ Detect Spam Comment
Spam words:

make a lot of money

buy now

click this

s1 = "make a lot of money"
s2 = "buy now"
s3 = "click this"

message = input("Enter your comment: ")

if s1 in message or s2 in message or s3 in message:
    print("This is spam!")
else:
    print("This is not a spam")
# 🧠 Logical Operators
Operator	Meaning
and	Both conditions must be true
or	At least one condition is true
not	Reverses the condition
# 📝 Practice Set (Chapter 6)
## Q5️⃣ Find the Greatest of 4 Numbers
a1 = int(input("Enter no. 1: "))
a2 = int(input("Enter no. 2: "))
a3 = int(input("Enter no. 3: "))
a4 = int(input("Enter no. 4: "))

if a1 > a2 and a1 > a3 and a1 > a4:
    print("Greatest number is a1:", a1)

elif a2 > a1 and a2 > a3 and a2 > a4:
    print("Greatest number is a2:", a2)

elif a3 > a1 and a3 > a2 and a3 > a4:
    print("Greatest number is a3:", a3)

else:
    print("Greatest number is a4:", a4)
# 🔧 Conditional Statements
## Basic If–Else
a = int(input("Enter your age: "))

if a >= 18:
    print("You can drive")
else:
    print("You cannot drive")
## If–Elif–Else
a = int(input("Enter your age: "))

if a >= 18:
    print("You can drive")
    print("Good! go for driving")

elif a < 0:
    print("You are entering negative age")

else:
    print("You are below the age")
## Small Test
age = int(input("Enter your age: "))

if age >= 18:
    print("yes")
else:
    print("no")


#PYTHON PRACTICE PROGRAMS (CHAPTER 7)

Q1. Write a program to find whether the given number is prime or not.
n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
Q2. Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter the number: "))
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)
Practice Set – Chapter 7
Q1. Write a program to print the multiplication table of a given number using for loop.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")
Q2. Write a program to get all the person names stored in a list which start with “S”.
names = ["Vidhi", "Saba", "Sahil", "Vikram"]

for name in names:
    if name.startswith("S"):
        print(f"Hello {name}")
Output:

Hello Saba
Hello Sahil
Q3. Do the 1st question again using while loop.
n = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(f"{n} × {i} = {n * i}")
    i +=1
