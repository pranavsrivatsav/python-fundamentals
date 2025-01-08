#Lists

#They are nothing but arrays, 
# and in python just like in javascript, lists can contain elements of different data types

#inbuilt methods of lists:
arr = [35,345,"345",True,346,6,67,8,567,45646,478,56345,]

#append
arr.append(567)
print(arr)

#pop
arr.pop()
print(arr)

#insert
arr.insert(0, 1)
print(arr)

#remove
arr.remove(67)
print(arr)

#extend
arr2 = ["345","sdfsfg","fdsd"]
arr.extend(arr2)

#index  - search method (start and end index to perform the search can be identified)
index1 = arr.index("345")
index2 = arr.index("345", index1+1)
index3 = arr.index("345", 0, index2)

print("index1", index1)
print("index2", index2)
print("index3", index3)

#count
print(arr.count("345"))

#reverse
arr.reverse()
print(arr)

#sort
#-------
#sort can only be done on lists which have elements of same data type

arr = ["orange", "mango", "grapes", "apple"]

#ascending
arr.sort()
print(arr)

#descending
arr.sort(reverse=True)
print(arr)

#sort with a key - nothing but a function that dictates the sort
#for a simple example - let us perform sort operation by providing the key
#as the inbuilt len function - will sort the list based on the length
arr.sort(key=len)
print(arr)
#-------

#slicing
print(arr[2:4])

#list comprehension 
#Creating a list by performing an operation on each element of an iterable entity
# syntax [expression for item in iterable if condition]
arr1 = ["orange", "pomegranate", "pineapple", "avocado"]
lenArr = [len(x) for x in arr1]
print(lenArr)
