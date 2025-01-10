"""
- 4 Qualities of sets
    1. Unique
    2. Unordered
    3. Mutable
    4. No indexing or slicing - since they are unordered


- Creation of sets in 2 ways
    1. using {}
    2. using set container passing an iterable entity like a list or tuple or even a string

- 3 Set operations
    1. insertion - add()
    2. removal
        2.1 remove() - throws error if element not found
        2.2 discard() - does not throw error if element not found
        2.3 pop() - will remove a random element from the set
    3. clear - clear()

- 4 Mathematical set operations
    1. Union
    2. intersection
    3. Difference - Returns elements only in set 1
    4. Symmetric difference - Returns elements that only exist in one of the 2 sets

- 5 Other operations
    1. length using len - len(<set>)
    2. check for an element using in - <element> in <set>
"""

#set creation
s = {'a', 'b', 'c', 'a'}
print(s) #Output: {'c', 'a', 'b'} - it will remove 2nd 'a' even though we have it during initialization

s = set(['a', 56, True])
print(s)

s = set('asdfkjshfl')
print(s) #will store only the unique chars part of the provided string

#--------------------------
#set operations

s.add('p')
print(s)

# s.remove('x') #error - since x is not present
s.discard('x') #no error

print(s.pop(), s) #remove random element from set

s.clear()
print(s) #output - set()

#--------------------------
#Mathematical set operations

#Union
s = set('Hello')
m = set('World!')
n = s | m
print(n)

#intersection
n = s & m
print(n)

#difference
n = s - m
print(n)

#symmetric difference
n = s ^ m
print(n)

#---------------------------------
#other operations

#length
print(len(n))

#find if element present
print('!' in n)