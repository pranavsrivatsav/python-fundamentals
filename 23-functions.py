"""
- Basic function definition syntax
def <funcName>(args):
    ...code

- Function with default args

- Function calls using named arguments

- 2 ways of creating functions accepting Variable arguments

- lambda functions

- nested functions

- function scope - nested functions

- function scope - local and global
"""


# ------------------------------------------------
# Basic function definition
def demoFunc(name):
    print(f"Hello {name}")


demoFunc("John")


# -----------------------
# function with return
def demoFunc(name):
    return "Hello " + name + "!"


print(demoFunc("VAughn"))


# -----------------------
# function with default args
def demoFunc(name="Jane"):
    return "Hello " + name + "!"


print(demoFunc())


# -----------------------
# Calling function with named args
def demoFunc(name, age):
    print(f"Hi! I am {name}. I am {age} years old")


# -----------------------
# calling using named args is very useful, as we can disregard the order of the arguments
demoFunc(age=25, name="Leo")


# -----------------------
# Accepting variable number of arguments
# method 1 - *args
def demoFunc(*args):
    # using args method: the arguments provided are stored as a tuple
    print(f"Hi! I am {args[0]}. I am {args[1]} years old")


demoFunc("Matt", 45)


# method 2 - **kwargs
def demoFunc(**kwargs):
    # using kwargs method: the arguments provided are stored as a dictionary
    print(f"Hi! I am {kwargs["name"]}. I am {kwargs["age"]} years old")


demoFunc(name="Keith", age=35)

# -----------------------
# lambda functions - one line anonymous functions using the lambda keyword used for simple evaluations
# variable = lambda <arg1, arg2...>: expression
squared = lambda x: x**2

# no explicit return in lambda - automatically the expression evaluated is returned
print(squared(13))


# -----------------------
# nested functions


# Inner function accessing variable without modifying from outer function
# This can be done naturally
def outerFunc(name):
    retStr = "Hi!" + name

    def innerFunc():
        print(retStr)

    innerFunc()


outerFunc("Kat")

# -----------------------
# Function scope - between inner and outer functions


# Inner function manipulating variable in outer function
# This cannot be done naturally
# if we try to perform operations in the inner function,
# inner function attempts to create a new variable in its scope

# ERROR EXAMPLE----
# def outerFunc(name):
#     retStr = "Hi!" + name

#     def innerFunc():
#         retStr += "....." #UnboundLocalError: cannot access local variable 'retStr' where it is not associated with a value
#         print(retStr)

#     innerFunc()

# outerFunc("Kat")
# -----------------


# Accessing and manipulating variables of outer function inside inner function
# This requires the usage of the keyword nonlocal
def outerFunc(name):
    retStr = "Hi!" + name

    def innerFunc():
        nonlocal retStr  # we have to first specify that the variable is nonlocal and then start using it
        retStr += "....."  # UnboundLocalError: cannot access local variable 'retStr' where it is not associated with a value
        print(retStr)

    innerFunc()


outerFunc("Kat")

# -----------------------
# Function scope - global and local

x = "global"


def demoFunc():
    x = "local"
    print(x)  # local


demoFunc()

print(x)  # global


# Accessing global variable without manipulating
# we can access it naturally
x = "global"


def demoFunc():
    print(x)  # global


demoFunc()

print(x)  # global


# Accessing global variables to manipulate
# we need to use global keyword
x = "global"


def demoFunc():
    global x
    x = "global local"
    print(x)  # global local


demoFunc()

print(x)  # global local
