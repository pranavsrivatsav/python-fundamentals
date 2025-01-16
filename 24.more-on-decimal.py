"""
- importing decimal
- Initializing a decimal
- controlling precision
- controlling rounding up
- An example of real world calculation using decimal
"""

#--------------------------------
# importing decimal
 
from decimal import Decimal, getcontext, ROUND_HALF_UP

#--------------------------------
# initializing decimal
x = Decimal(1)
y = Decimal(1.0)
z = Decimal("1.0")

print(x == y == z)

x = Decimal(1.59283498) # Initialization using float not recommended
y = Decimal("1.59283498") 
print(x == y) # True
print(x + x) # 3.185669959999999800714931553
print(y + y) # 3.18566996
print((x + x) == (y + y)) # OP: false - Precision issues because of initializing using float


#--------------------------------
# controlling precision

#set precision
getcontext().prec = 6

x = Decimal("1.1234566")
y = Decimal("3.1564520")

print(x + y) #op: 4.27991


#--------------------------------
# controlling rounding up

# We use the quantize method to perform rounding up

#----------
# 1. ROUNDING UP to fixed number of decimal places

x = Decimal("1.11534345")

# As the first argument of the quantize method, we just provide a decimal,
# the value of the decimal does not matter, all matters is the no of digits after
# the point, based on which the rounding up will be done
print(x.quantize(Decimal("2.1111")))
print(x.quantize(Decimal("1.0000")))


# Further there are additional rounding methods, that we can use

# ROUND_CEILING: Rounds towards positive infinity (up).
# ROUND_DOWN: Rounds towards zero (truncates).
# ROUND_FLOOR: Rounds towards negative infinity (down).
# ROUND_HALF_DOWN: Rounds towards zero when halfway.
# ROUND_HALF_EVEN: Rounds towards the nearest even number (default).
# ROUND_HALF_UP: Rounds away from zero (up).
# ROUND_UP: Rounds away from zero (always rounds up).
# ROUND_05UP: Rounds to the nearest multiple of 0.5.

# An example of how to use the rounding method
x = Decimal("1.11155")
y = Decimal("1.11156")
z = Decimal("1.11154")
print(x.quantize(Decimal("1.0000"), ROUND_HALF_UP)) #OP: 1.1116 - rounded up since halfway
print(y.quantize(Decimal("1.0000"), ROUND_HALF_UP)) #OP: 1.1116 - rounded up since above halfway
print(z.quantize(Decimal("1.0000"), ROUND_HALF_UP)) #OP: 1.1115 - rounded down since below halfway

"""
Explanation for above output:
- we use the rounding mode ROUND_HALF_UP - it will always round up from half way.
"""


#--------------------------------
# An example of real world calculation
gst_calculator = lambda x : Decimal("1.18") * Decimal(str(x))

print(gst_calculator(1023))