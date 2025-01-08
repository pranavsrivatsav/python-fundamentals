# comparison operators

#--------------------------------------------------
# with integers
a = 10
b = 3

# greater than
print(a > b) # True

# lesser than
print(a < b) # False

# greater than or equal to
print(a >= b) # True

# lesser than or equal to
print(a <= b) # False

# equal to
print(a == b) # False

# not equal to
print(a != b) # True


print("--------------------------------------------------")
# with strings - Performs lexicographical comparison (i.e dictionary ordering)
# and lowercase takes precedence over upper case i.e (a > A)

str1 = "Small"
str2 = "SmalL"

# greater than
print(str1 > str2) # True

# lesser than
print(str1 < str2) # False

# equal to
print(str1 == str2) # False

# not equal to
print(str1 != str2) # True


print("--------------------------------------------------")
# with boolean

# True takes precedence over false
# because in binary terms (true = 1 and false = 0)

# greater than
print(True > False) # True

# lesser than
print(True < False) # False

# equal to
print(True == False) # False

# not equal to
print(True != False) # True

# True is 1
print(True == 1) # True

# False is 0
print(False == 0) # True

# well well, since Boolean is technically integers
# we can perform arithmetic operations as well
# I think i have a love-hate relationship with dynamically typed languages
print (1 + True) # 2
print (1 + False) # 1
print (True + False) # 1