# Logical Operators

# and
# or
# not

# ----------------------------------------
# numbers
# 1. Python considers any non 0 integer is inferred in boolean terms as true and 0 is inferred in boolean terms as false
# 2. and - if left value is true, right value is checked and if true right value is returned, else 0 is returned, if left value is false 0 is returned
# 3. or - if left values is true - left value is returned, if left is false, right is checked, if right is true right value is returned, else 0 is returned

# and operation between integers always returns an integer
print(3 and 0)
print(3 and 2)

print("------")
# or operation between integers always returns an integer
print(3 or 0)
print(0 or 3)

print("------")
# not operation always returns a boolean - it provides the boolean result
# based on the boolean inference of the integer value
print(not 0)
print(not 3)

print("----------------------------------------")
# strings


# The output of the boolean operations between the strings depends on the following things:

# 1. Python considers empty strings as having a boolean value of the ‘false’ and non-empty strings as having a boolean value of ‘true’.
# 2. For the ‘and’ operator if the left value is true, then the right value is checked and returned. If the left value is false, then it is returned
# 3. For the ‘or’ operator if the left value is true, then it is returned, otherwise, if the left value is false, then the right value is returned.

print("x" and "")  # ""
print("x" and "a")  # "a"
print("x" and "X")  # "X"
print("X" and "x")  # "x"
print("" and "a")  # ""

print("------")

print("x" or "")  # "x"
print("x" or "a")  # "x"
print("x" or "X")  # "x"
print("X" or "x")  # "X"
print("" or "a")  # "a"

print("------")
print(not "x")  # False
print(not "")  # True

print("----------------------------------------")
# boolean

print(True and False)  # False
print(True or False)  # True


print("----------------------------------------")
# numbers with boolean
print(1 and True)  # True
print(1 and False)  # False
print(0 and True)  # 0
print(0 and False)  # 0

print("------")

print(1 or True)  # 1
print(1 or False)  # 1
print(0 or True)  # True
print(0 or False)  # False

print("------")

print(True and 1)  # 1
print(False and 1)  # False
print(True and 0)  # 0
print(False and 0)  # False

print("------")

print(True or 1)  # True
print(False or 1)  # 1
print(True or 0)  # True
print(False or 0)  # 0
