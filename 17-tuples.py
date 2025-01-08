# Tuples - non mutable lists 

# They are created using ()
# They are faster than lists - so if possible use them in supporting scenarios

a = ("John",36,"Male")
print(a)

#we cannot reassign or manipulate tuples - will throw an error
# a[0] = "Jane" #error: TypeError: 'tuple' object does not support item assignment

#all the non manipulative methods of lists should work for tuples as well
print(a.index("John"))
print(a.count(36))

#converting to list
arr = list(a)
print(arr)

#convert list to tuple
a = tuple(a)
print(a)

#unpacking tuples into individual variables - the count of variables at LHS should match tuple size
l,m,n = a
print(l,m,n)

# x,y = a #ValueError: too many values to unpack (expected 2)
# l,m,n,o = a #ValueError: not enough values to unpack (expected 4, got 3)
