# to use a module first we need to import it, like here we want to use the random module.
import random

# random.randint(range1, range2) -> function which returns a random integer between 2 ranges including the ranges integers.

random_integer = random.randint(1,10)
print(random_integer)

# module -> What is a module? distributed part of code, to be used in a collaborative manner. It's a class basically when compared to Java.

# You can create and use your own module, eg here we created myModule.py and are now importing it in this .py file.

import myModule

print(myModule.pi)

# random floating point numbers -> random.random() -> Returns the next random floating point number between [0.0 to 1.0) without including the ranges.

random_float = random.random()
print(random_float)

random_float * 5 #random floats between 0 and 5 but excluding these ranges (0 & 5)

# random.uniform(a, b) -> Returns a random floating point N such that a <= N <= b if a <= b and b <= N <= a if b < a.

# this function can be used in multiple scenarios -> love calculator, throw dice, flipping coin or games etc.
