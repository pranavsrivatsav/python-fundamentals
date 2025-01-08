# String manipulation exercises

# 1. Reverse a string

# 1.1 - using a loop
# 1.1.1 - my ugly method
str = input("Enter a string: ")
length = len(str)
reverseStr = []

i = length - 1
while i >= 0:
    reverseStr.append(str[i])
    i -= 1

reverseStr = "".join(reverseStr)
print(reverseStr)

# 1.1.2 - chat gpt's simple and brilliant logic
reverseStr = ""
for char in str:
    reverseStr = char + reverseStr

print(reverseStr)

# 1.2 using slice
reverseStr = str[::-1]
# Providing only the split step without start and end indices just starts splitting
# the string into
print(reverseStr)

reverseStr = str[
    -1::-1
]  # this works as well - as we ask it to start from last character
print(reverseStr)

# 1.3 using inbuilt reversed function
reverseStr = "".join(reversed(str))
print(reverseStr)


# 2. check palindrome - we'll just extend the logic from the first
if reverseStr == str:
    print(str, "is a palindrome")
else:
    print(str, "is not a palindrome")

# 3. count the no of vowels in the string
vowelList = ["a", "e", "i", "o", "u"]
vowelCount = 0
for char in str:
    if char in vowelList:
        vowelCount += 1
print("vowelcount:", vowelCount)

# 4. Remove duplicates
duplicateRemovedStr = str[:]
for char in str:
    indexChar = duplicateRemovedStr.find(char)
    # split string until the index and from the remaining part of the string replace the chars with ''
    duplicateRemovedStr = duplicateRemovedStr[: indexChar + 1] + duplicateRemovedStr[
        indexChar + 1 :
    ].replace(char, "")

print(duplicateRemovedStr)

#5. Text wrap
lineLength = 20

if(len(str) > lineLength):
    displayString = str[:lineLength] + "\n" + str[lineLength:]
    print(displayString)

#6. String slicing
print(str[:3]) #first 3 chars
print(str[-3:]) #last 3 chars
print(str.title()) #capitalize each word


