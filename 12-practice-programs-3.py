# Practice - For loop
# -----------------------------------------
# 1. sum of numbers
num = int(input("Enter a number: "))
sum = num

for i in range(num-1, 0, -1):
    sum += i

print(sum)

# -----------------------------------------
# 2. Factorial
num = int(input("Enter a number: "))
factorial = num

for i in range(num-1, 1, -1):
    factorial *= i

print(factorial)

# -----------------------------------------
# 3. Print a Pattern
num = int(input("Enter number of rows: "))
for i in range(1, num+1, 1):
    row = ["*"] * i
    
    for char in row:
        print(char, end='')
        
    print()
    
# -----------------------------------------
# 4. Check for prime number
num = int(input("Enter a number: "))
isPrime = True
for i in range(num-1, 1, -1):
    
    if(num % i == 0):
        isPrime = False
        break
    
output = "num is " + ("prime" if isPrime else "not a prime")
print(output)
        
# -----------------------------------------
# 5. List manipulation
numArr = input("Enter a list of numbers (separated by a space): ")
numArr = numArr.split()

sum = 0
max = int(numArr[0])
min = int(numArr[0])
evenArr = []

for num in numArr:
    
    num = int(num)
    
    # update sum
    sum += num
    
    # update max
    if(num > max):
        max = num
        
    # update min
    if(num < min):
        min = num
        
    # update evenArr
    if(num % 2 == 0):
        evenArr.append(num)
        
print("sum: ", sum)
print("max: ", max)
print("min: ", min)
print("even nums: ", evenArr)
    