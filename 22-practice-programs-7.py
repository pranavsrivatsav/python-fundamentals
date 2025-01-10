# Practice programs sets and dictionaries
#--------------------------------------------
#Find frequency of a word in the sentence
sentence = "Create two sets of numbers. Find and print the symmetric difference between the two sets"
sentenceSet = set(sentence.split())
sentenceDict = {}
for word in sentenceSet:
    sentenceDict[word] = sentence.count(word)

print(sentenceDict)

#--------------------------------------------
#Unique vowels in the string
vowelList = ['a', 'e', 'i', 'o', 'u']
sentence = "Create two sets of numbers. Find and print the symmetric difference between the two sets"
vowelSet = set()
for char in sentence:
    if char in vowelList:
        vowelSet.add(char)

print(vowelSet)

#--------------------------------------------
#check one set is a subset of another
subset1 = {1,2,3,4,5,6}
subset2 = {2,3,5}
unionset = subset1 | subset2

print(unionset == subset1)

#--------------------------------------------
#invert dictionary
dict1 = {1:10, 2:20, 3:30}
dict2 = {}

for key,value in dict1.items():
    dict2[value] = key

print(dict2)

#--------------------------------------------
#group by value
"""
Given a dictionary, group the keys based on their values and create 
a new dictionary where the keys are the values and the values are lists of keys that 
share that value.
"""

dict1 = {1:10, 2:20, 3:30, 4:10, 5:10, 6:30}
dict2 = {}

for key, value in dict1.items():
    dict2Entry = dict2.get(value)

    if(dict2Entry):
        dict2Entry.append(key)
    else:
        dict2[value] = [key]

print(dict2)
    