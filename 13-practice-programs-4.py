# Practice - While loop
# -----------------------------------------

import random

# 1. Countdown

num = 5
while(num > 0):
    print(num)
    num-=1
    
print("Take off!")

# -----------------------------------------
# 2. Sum of even numbers
num = int(input("Enter a number: "))
sumEven = 0

while(num > 0):
    if(num %2 == 0):
        sumEven += num
        
    num -= 1

print("sum of even numbers: ", sumEven)
              
# -----------------------------------------
# 3. Guessing Game
rand = random.randint(1, 100)
guess = None

while(guess != rand): 
    guess = int(input("Guess the number: "))
    
    if(guess > rand):
        print("Go lower!")
    elif(guess < rand):
        print("Go higher")
    else:
        print(f"Bingo! indeed it is {guess}")

# -----------------------------------------
# 4. Fibonacci Sequence
num = int(input("Enter a number: "))
sequence = [0, 1]
length = len(sequence)

if(num == 1):
    sequence = [0]
else:
    while(length < num):
        sequence.append(sequence[length -1] + sequence[length -2])
        length = len(sequence)

print(sequence)
    
# -----------------------------------------
# 5. User input validation
num = 0
while(num < 1):
    num = int(input("Enter a positive integer: ")) 