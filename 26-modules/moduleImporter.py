"""
index:
- import demo
- import with alias
- import selectively from a module
- import everything from a module
- import selectively with alias from a module
- check if running script is imported or not using __name__
"""

#-----------------------------------------
# import demo

# import myMath

# print(myMath.squared(6))
# print(myMath.add(6,7))

#-----------------------------------------
# importing with alias demo

# import myMath as m

# print(m.squared(6))
# print(m.add(6,7))

#-----------------------------------------
# importing selectively from a module

# from myMath import add

# print(add(7,8)) #no need to call add as myMath.add

#-----------------------------------------
# importing everything from a module

# from myMath import *

# print(add(7,8))
# print(squared(7))


#-----------------------------------------
# importing selectively with alias from a module
# from myMath import add as sum, squared as sq

# print(sum(89,90))
# print(sq(8))

#-----------------------------------------
# checking if the script running is imported or not using __name__
# from myMath import nameCheck
# print(__name__) #running script not imported
# nameCheck() #running script imported

#__name__ will provide the module name
