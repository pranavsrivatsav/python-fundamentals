# Strings

#------------------------------------
#1. String indexing

str = "Demo"
print(str[0], str[-1])

#------------------------------------
#2. String slicing

str1 = "Hello world"
print(str1[1:3]) #start index - inclusive | end index - exclusive
print(str1[:7]) #default start index - 0
print(str1[1:]) #default end index - string length
print(str1[:]) #just returns the entire string
print(str1[2:10:2]) 
#the third param is step size 
#- basically number of characters it counts before slicing a character from a string
print(str1[::2]) #slices the entire string with step size 2

print(str1[::-1]) #slices the entire string but with step size -1
#basically this will start slicing the string in reverse 1 step at a time

print(str1[::-2]) #reverse slice the string, but with step size 2

#------------------------------------
#3. String methods

#3.1 String case methods
str2 = "Faber CASTELL"
#3.1.1 upper
print(str2.upper())

#3.1.2 lower
print(str2.lower())

#3.1.3 capitalize
print(str2.capitalize())

#3.1.4 title
print(str2.title())

#--------

#3.2 Other methods
str3 = "red blood blue blood"

#3.2.1 count
print(str3.count("bl"))

print(str3.count("bl", 9, 13)) #start index - inclusive | end index - exclusive

print(str3.count("bl", 9))

print(str3.count("bl", None , 9))

#3.2.1 find
print(str3.find("bl")) #index of first instance

print(str3.find("bl", 9, 12)) #start index - inclusive | end index - exclusive

#3.2.1 replace
print(str3.replace("bl", "BL"))

print(str3.replace("bl", "BL", 2)) #No of occurences to replace (default: -1 means replace all occurences)

#3.2.1 split
str4="It has been a   LONG wait"
print(str4.split()) #by default all whitespace characters are taken as delimiters (\n, \t, \r, \f and all blank spaces)

str5 = "dry-cough-formula-syrup"
print(str5.split('-'))

print(str5.split('-', 2)) #Max no of splits to make using the delimiter

#3.2.1 join
str6 = " | "
fruits = ["orange", "apple", "grapes", "mango"]

print(str6.join(fruits))
