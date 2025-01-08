#While loop
#----------------------------------------

#Case 1: Normal while loop
print("----------------------------------------")
i = 5

while(i > 0): 
    i-=1
    print(i)


print("lift off!")

#Case 2: While loop with break
print("----------------------------------------")
i = 5

while(i > 0): 
    if(i==2): 
        break
    print(i)
    i-=1


print("break off!")

#Case 3: While loop with continue
print("----------------------------------------")
i = 5

while(i > 0):
    i-=1 
    if(i%2 == 0): 
        continue
    print(i)


print("continue odd!")
