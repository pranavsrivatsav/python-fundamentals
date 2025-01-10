from decimal import Decimal, getcontext

"""
Float: Float is used to store numbers with decimals.

Pros and Cons of float:

Pros:
-> Less storage space
-> Faster calculations

Cons:
-> Less precision yielding unexpected results

Best usage scenario: To store decimal point numbers, which might not be used in calculations
"""
a = 0.1 + 0.2
b = 0.3
print(a == b)

"""
Decimal: Decimal is used to store numbers with more precision and for more precise calculation

Pros and Cons of Decimal:

Pros:
-> More precise calculations yielding less unexpected results

Cons:
-> More storage space
-> Needs import of decimal package to use

Best usage scenario: to store decimal point numbers which will be used in precise calculations
"""

# Decimals can be initiated using int, float and string
# Initiation using string is better practice, as it yields more precision
x = Decimal(0.1) + Decimal(0.2)
z = Decimal(0.3)

print(x==z) #False - because we are initiating using float

x = Decimal("0.1") + Decimal("0.2")
z = Decimal("0.3")

print(x==z) #True - because we are initiating using a string


"""
We can combine usage of decimal and float types

During the calculation phase, we can use decimals
Once the result is obtained,
we can store the result in float as it requires less storage, 
but the result will be rounded off until the precision that can
be handled by float
"""
m = Decimal('56.45345354')
n = Decimal('24.242423423423434')
o = m * n
p = float(o)
print(p,o, p==o) #we can see that p is a rounded off version of o 
