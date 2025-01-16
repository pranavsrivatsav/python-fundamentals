"""
This presence of __init__.py file in a folder indicates that the folder is a package.

A package is nothing but a collection of related modules.

The __init__.py file will contain the initialization code for the package.

A package name should follow all the rules of an identifier:
- should not be a keyword
- should not start with a number
- should not have any other characters except alphabets, numbers and _

Similarly a module inside the package should also follow the naming rules of python
- should not be a keyword
- should not start with a number
- Only lowercase letters, numbers, and underscores are allowed. (strangely our repo files with "-" are working, but they cannot be imported)
"""

"""
All types of imports:

Absolute import: import my_package.module1
Relative import: from .module1 import function_from_module1
Importing from a subpackage: import my_package.subpackage.submodule
Simplifying imports in __init__.py: Import common functions or classes into the package’s __init__.py
"""

# from mypackage import module1 as m1, module2 as m2
# or
import mypackage.module1 as m1, mypackage.module2 as m2

print(m1.squared(2))
print(m2.add(89,90))
print(m2.cube(4))