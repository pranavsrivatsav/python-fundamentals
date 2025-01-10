"""
- 4 qualities of dictionary
    - unordered key value pairs
    - mutable
    - unique keys
    - immutable keys - can only be of immutable data types like strings, int, float etc.

- 2 ways of creating a dictionary
  - using {<key1>:<value1>, <key2>:<value2>}
  - using dict constructor

- 2 ways of accessing a dictionary
  - using [<key>] - will throw error if key not present
  - using get() - will return None if key not present, can specify default return value if key not present

- method to modify a dictionary
  - using [<key>] -> we can modify the value of a key, or insert a new key-value pair

- 4 methods to remove items in a dictionary
  - del keyword
  - pop - to remove the entry of specified key
  - popitem - to remove last key-value pair, used in ordered dictionary, a data type part of latest python versions
  - clear

- 4 other built in dictionary methods
  - keys
  - values
  - items: an iterable view object with all key-value pairs included as tuples
  - update: a method to merge dicts

- 3 ways to loop through a dictionary
    - loop through keys
    - loop through values
    - loop through items

- dictionary comprehension
    - similar to list comprehension 
        - eg: newDict = {<key>: <expression> for iterator in iterable}

- nested dictionaries
    - we can nest dictionaries just like I suppose we can nest lists

- real world usage scenarios for dictionary
    - config files
    - mappings etc.

"""
#------------------------------------
#create a dictionary
dict1 = {
    "name": "person", #Here quotes need to be provided for string keys
    "age": 26
}
print(dict1)

dict1 = dict(name= "person", age= 26) #Here quotes need not be provided for string keys
print(dict1)

#------------------------------------
#Accessing a dictionary
print(dict1["name"])
print(dict1.get("name"))

# print(dict1["city"]) #KeyError: 'city'
print(dict1.get("city")) 
print(dict1.get("city", "Unspecified")) #default value if key not found

#------------------------------------
#Modifying a dictionary
dict1["name"] = "Matt" #existing key
dict1["city"] = "Chicago, NY" #new key-value
print(dict1)


#------------------------------------
#Removing items in a dictionary
del dict1["city"]
print(dict1)

dict1["city"] = "Chicago, NY"
dict1.pop("city")
print(dict1)

dict1["city"] = "Chicago, NY"
dict1.popitem()
print(dict1) 
#for pop in unordered dictionary - the removal will be arbitrary
#useful in ordered dictionary - which is a part of the latest python versions

dict1.clear();
print(dict1)


#------------------------------------
#Other built in methods

dict1 = {'name': 'Matt', 'age': 26, 'city': 'Chicago, NY'}
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# update argument can be another tuple or an iterable containing tuples of (key, value)
dict1.update({'pincode':  '76853', 'age': '27'})
print(dict1)

dict1.update([('pincode',  '768434'), ('age', '37')])
print(dict1)

#------------------------------------
#looping through a dictionary

for key in dict1.keys():
    print(key)


for value in dict1.values():
    print(value)


for item in dict1.items():
    print(item)

#------------------------------------
#dictionary comprehension
squaredDict = {x: x**2 for x in range(1,11)}
print(squaredDict)

#------------------------------------
#nested dictionaries
nestedDict = dict(dictionary = dict1, count = 1)
print(nestedDict)