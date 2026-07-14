# print to the console
print("Hello, World!")

# import the "sys" package to check the python version of the system
import sys
print (sys.version)

# checking/learning indentation
if 1 < 2:
    print('i am correct')


# learning variable declaration
name = "grace"
age = 10
print(name, age)

# connecting different syntax/code on same line
print(1); print("true"); print("alter")

print("Hello World!", end=" ")

print("Oh no!")

print("Hello World!", "Oh no!")

# more on print function
print(2*2+2-2/2)
print(2/2)
print(2-2)
print(2+2)
print(3/3)
print("a" + "b" + "c")

# comments
"""
This is a comment
"""
#this is also a comment

"""
fgyfi
dfghds
fgfdsh
dighdsi
"""

# using casting; casting is the act of producing a value in a new type
# it can be used to specify the data type of a variable, but it doesn't change it's data type
x = str(3)
p = int(3)
fp = float(4)

x = 5 
str(x)
print(x)

xi = 6
str(xi)
print(type(xi))
# avoiding crash/panic
try:
    int("grace")
except ValueError:
    print("noo")


# more on variable declaration
_ = "grace"
print(_)

nt, yv, gg = "grace", "int", 7
print(nt, gg)


fruit = ["banana", "mango", "apple"]
print(fruit)
ff, qq, rr = fruit
print(ff +  qq + rr)

try:
    rrr = "grace "
    ee = "loves "
    fff = 2
    print(rrr + ee + fff)
except TypeError:
    print("number")

# 

x = 5j
print(x,type(x))

x = 2
y = 2.3
z = 1j


a = float(x)
print(type(a))
# you cannot convert complex number to another type e.g  x = 2j; d = int(x); print(type(d))

# random numbers
# this will print any random number within that range
import random
print(random.randrange(1, 10))


# more on strings
# using quote in strings, you can use quote in strings so long as they donot match
print("i am 'omahlay'")
print('my name is "omahlay"')

# multiline strings
a = '''i am a girl who loves coding
my name is Omale Ooja Grace'''
print(a)

# strings are arrays
a = "i am coming"
print(a[9])

# looping through strings

for z in "my own":
    print(z)

# getting length of strings
q = "coming"
print(len(q))

# checking if a character/phrase is present in a string, you use the "in" keyword
txt = "no am not"
print("no" in txt)
if "no" in txt:
    print("available")
else:
    print("e dey")

# this checks if it is not present in a string
if "no" not in txt:
    print("available")
else:
    print("e dry")

# Slicing 

g = "Hello, world"
print(g[1:4]) #this slice excludes the 4th index
print(g[:4]) #this will give "Hell" i.e leaving the 4th index, giving from start to 4th
print(g[4:]) #this will print everything from the 4th index i.e "o, world"
print(g[-5:-2]) #this will print "wor"
print(g[-2:-5])
"""this will print an empty string because slicing works in one direction i.e left to right
when the position is past the end there is nothing to walk through"""

# string modification

a = " coMIng,home "
print(a.upper()) #this uppercase all the characters in a
print(a.lower()) #this lowercase all the characters in a
print(a.strip()) #this removes all trailing whitespace at the start and end of a string
print(a.replace("c", "r"))
"""this replaces a string with another string
if the string to be replaced does not exist within it, it won't have an effect"""
print(a.split(",")) #splits string into substrin if it finds the separator u put in 

# string concatenation
a = "my"
b = "name"
d = " "
c = a + d +b
print(c)

# String format
"""We cannot combine a string and int like this
num = 34; txt = "i am" + num 
that will give an error, So we use the format, f"""
age = 23
word = f"i am {age:x} years old"
print(word)


