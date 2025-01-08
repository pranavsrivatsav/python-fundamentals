# --------------------------------------------
# DMAS of input
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("add", a + b)
print("sub", a - b)
print("div", a / b)
print("mul", a * b)


# --------------------------------------------
# Area of Circle
radius = int(input("Enter radius: "));
area = (radius ** 2) * 3.14
print("circle area:", area);

# --------------------------------------------
# Temperature Conversion
inputTemp = float(input("Enter input temperature: "))
inputUnit = str.lower(input("Enter input unit ('f' - fahrenheit | 'c' - celsius): "))
outputUnit = "f" if inputUnit == "c" else "c"
outputTemp = (
    ((inputTemp * (9 / 5)) + 32) if outputUnit == "f" else ((inputTemp - 32) * (5 / 9))
)

print(str(outputTemp) + str.upper(outputUnit))


# --------------------------------------------
# String Manipulation
inputText = input("Enter a sentence: ")
lengthText = len(inputText) - 1; 
print("length:", len(inputText.split(' ')))
print("First character:", inputText[0])
print("Last character:", inputText[lengthText])


# --------------------------------------------
# Swap values
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("num1: ", num1)
print("num2: ", num2)
