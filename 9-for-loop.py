#for loop
#-----------------------------------------------------
#Case 1: Looping through an iterable entity
#1.1. Looping through a string
print("--------------------------------------------")
msg = "abcdef"
for char in msg:
    print(char)
        
#1.2. Looping through a list
print("--------------------------------------------")
fruits = ["apple", "mango", "orange"]
for fruit in fruits:
    print(fruit)

#1.3. Looping through a dictionary (set of key value pairs separated by a comma)
print("--------------------------------------------")
demodict = {"name": "Prince", "age": "25", "weight": "57kg"}
for key, value in demodict.items():
    print(f"{key}: {value}")

#-----------------------------------------------------
#Case 2: Looping through a defined range
#2.1. Looping through a simple defined range
print("--------------------------------------------")
for i in range(5): #0 to 4: -> 5 is exclusive
    print(i) 
    
#2.2. Looping through a range defined with start, stop and step
print("--------------------------------------------")
for i in range(10, 0, -2): #range(start, end, step) -> end is exclusive
    print(i)