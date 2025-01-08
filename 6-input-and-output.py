
#input

name = input("Enter your name: ")

#input is always obtained as a string, we can convert into other data types while assigning
age = int(input("Enter your age: "))


#Output

print("Hello","World")

print("Hello", name)

print("Hello "+name)

print(f"Hello {name} - {age}")