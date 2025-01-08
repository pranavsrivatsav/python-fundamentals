# Practice exercise - List and Tuples

#1. Do the following ops with a list of numbers
arr = [234, 23, 4556, 536, 4224]

#1.1 sum of all numbers
sum = 0
for num in arr:
    sum += num

print("sum", sum)

#1.2 max and min
sortedarr = arr[:]
sortedarr.sort()

print("min", sortedarr[0])
print("max", sortedarr[-1])

#1.3 new list with only even nums
evenArr = []
for num in arr:
    if(num%2 == 0):
        evenArr.append(num)

print("evenArr", evenArr)

#1.4 sort asc order
print("sorted", sortedarr)

#1.5 reverse list
reverseArr = arr[:]
reverseArr.reverse()
print("reverseArr", reverseArr)


#2 Unpack a tuple into individual elements
tup = (34, 'dfsf', True)
a,b,c = tup
print(a,b,c)


#3 Common elements between 2 lists
list1 = ["asjkdh", 23, True, "yuo"]
list2 = [45, "sfghkfds", True, "yuo"]

commonList = []

for el in list1:
    if(el in list2):
        commonList.append(el)

print(commonList)

#square of first 10 numbers using list comprehension
squaredNumArr = [x**2 for x in range(1,11)]
print(squaredNumArr)