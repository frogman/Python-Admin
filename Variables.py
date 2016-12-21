#PYTHON OPERATOR
#https://www.programiz.com/python-programming/operators


#int(x [,base])
#Converts x to an integer. base specifies the base if x is a string.

#long(x [,base] )
#Converts x to a long integer. base specifies the base if x is a string.

#float(x)
#Converts x to a floating-point number.

#complex(real [,imag])
#Creates a complex number.

#str(x)
#Converts object x to a string representation.

#repr(x)
#Converts object x to an expression string.

#eval(str)
#Evaluates a string and returns an object.

#tuple(s)
#Converts s to a tuple.

#list(s)
#Converts s to a list.

#set(s)
#Converts s to a set.

#dict(d)
#Creates a dictionary. d must be a sequence of (key,value) tuples.

#frozenset(s)
#Converts s to a frozen set.

#chr(x)
#Converts an integer to a character.

#unichr(x)
#Converts an integer to a Unicode character.

#ord(x)
#Converts a single character to its integer value.

#hex(x)
#Converts an integer to a hexadecimal string.

#oct(x)
#Converts an integer to an octal string.


#Python Strings
#!/usr/bin/python

str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

#Python Lists
#!/usr/bin/python

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd
print(list[2:])      # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist) # Prints concatenated lists

#Python Tuples - ReadOnly Lists
#!/usr/bin/python

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

#Pyhthon dictionaries
#Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.
#Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). For example −
#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

