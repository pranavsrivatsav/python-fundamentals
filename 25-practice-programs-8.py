# Practice programs functions
# --------------------------------------------


# Factorial recursive
def fact(num):
    if num < 2:
        return 1
    else:
        return num * fact(num - 1)


number = 5
print(fact(number))


# Temperature converter
def convert_temperature(value, unit):
    c2f = lambda x: (x * (9 / 5)) + 32
    f2c = lambda x: (x - 32) * (5 / 9)

    if unit == "C":
        return str(c2f(value)) + "F"
    else:
        return str(f2c(value)) + "C"


print(convert_temperature(value=32, unit="C"))
print(convert_temperature(value=89.6, unit="F"))

# global value incrementer
globalx = 10

def inc_global_x():
    global globalx
    globalx += 1

print(globalx)
inc_global_x()
print(globalx)
