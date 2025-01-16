# can import from other modules in the package
from . import module1

add = lambda x, y: x + y
sub = lambda x, y: x - y
cube = lambda x: module1.multiply(x, module1.squared(x))

