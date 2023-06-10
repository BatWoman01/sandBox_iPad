""" Data Types are defined as the type and range of values that it 
can have.
Variables are simply a name to which a value can be assigned. """

""" Numbers - 1, 2, 3, 4, 5, ..... """
# Integers
print(10) # Positive Integer
print(-3000) # Negative Integer

num = 123456789 # Assigning an integer to a variable
print(num)

num = -1600 # Assigning a new integer
print(num)

# Floating Point Numbers
print(1.0000000005) # Positive Float
print(-85.6701) # Negative Float

flt_pt = 1.23456789
print(flt_pt)
# In Python 5, 5 is an integer and 5.0 is a float.

# Complex Numbers - complex(real, imaginary)
print(complex(10, 20)) # Represents the complex number (10 + 20j)
print(complex(2.5, -18.2)) # Represents the complex number (2.5 - 18.2j)

complex_1 = complex(0, 2)
complex_2 = complex(2, 0)
print(complex_1)
print(complex_2)

""" Booleans - True or False
    Also known as bool
    Allows us to choose between 2 values: true and false
    The first letter of a bool needs t be capatilized in Python. """
print(True)

f_bool = False
print(f_bool)

""" Strings - "Hello, World", "VR is interesting gameplay"
    Is a collection of characters iclosed within single, double, or triple quotation marks """
print("Harry Potter!") # Double quotation Marks

got = 'Game of Thrones... ' # Single quotation marks
print(got)
print("$") # Single character

multiple_lines = '''Triple quotes allows
multi-line string.'''
print(multiple_lines)

# The Length of a String
ran_str = "I am Batman" # 11 characters
print(len(ran_str))

# Indexing
batman = "Bruce Wayne"

first = batman[0] # Accessing the firt character
print(first)

space = batman[5] # Accessing the empty space in the string
print(space)

last = batman[len(batman - 1)] 
print(last)
# Reverse Indexing
print(batman[-1]) # Corresponds to batman[10]
print(batman[-5]) # Corresponds to batman[6]

# String Immutability
string = "Immutability"
string[0] = '0' # Will give error

str1 = "hello"
print(id(str1))

str1 = "bye" 
print(id(str1))

""" The None Keyword 
    It only has a single value, None.
    Can be assigned to any variable, but cannot create other NoneType variables."""

val = None
print(val) # prints "None" and returns None
print(type(val))

# None is not a default value for the variable that has not yet been assigned a value.
# None is not the same as False.
# None is not an empty String.
# None is not 0.

""" String Slicing
    The process of obtaining a portoin (substring) of a string by using  its indices. """
# Template: string[start:end]
# start us the index from where we want the substring to start.
# end is the index where we want our substring to end.

my_string = "This is MY string." 
print(my_string[0:4]) # From the start till the 4th index.
print(my_string[1:7])
print(my_string[8:len(my_string)]) # From the 8th index till the end.

# Slicing with a Strp
