# Practice - Conditional programming
# -----------------------------------------
# 1. Grade Calculator
score = int(input("Enter your score: "))
grade = None
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"grade: {grade}")

# -----------------------------------------
# 2. Odd or even
num = int(input("Enter a number: "))
if(num % 2 == 0): 
    print("even")
else:
    print("odd")

# -----------------------------------------
# 3. Leap year

year = int(input("Enter a year:"))
if(year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# -----------------------------------------
# 4. Max of 2 numbers
nums = input("Enter two numbers (separated by a space): ")
nums = str.split(nums)
    
if int(nums[0]) > int(nums[1]):
    print(f"Max: {nums[0]}")
else:
    print(f"Max: {nums[1]}")
    
# -----------------------------------------
# 5. Vowel or Consonant
char = input("Enter a character")
vowels = ["a", "e", "i", "o", "u"]

if(char in vowels):
    print("vowel")
else:
    print("consonant")
    
