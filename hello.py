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