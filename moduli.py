# Ask Python to print sqrt(25) on line 3.
import math
print(math.sqrt(25))

#However, we only really needed the sqrt function, and it can be frustrating to have to keep typing math.sqrt().
#It's possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it's done with the from keyword:

#from module import function
#Now you can just type sqrt() to get the square root of a number—no more math.sqrt()!

# Import *everything* from the math module on line 3!
#from math import *


#show all functions in math module
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything)       # Prints 'em all!

print("Uporedjivanje brojeva - ugradjene funkcije u python nisu potrebni moduli")
def biggest_number(*args): #zvjezdicom mozemo vise argumenata u nizu dodjeliti pozivanjem funkcije
    print(max( args ))
    return max( args )


def smallest_number(*args):
    print(min( args ))
    return min( args )


def distance_from_zero(arg):
    print(abs( arg ))
    return abs( arg )


biggest_number( -10, -5, 5, 10 )
smallest_number( -10, -5, 5, 10 )
distance_from_zero( -10 )