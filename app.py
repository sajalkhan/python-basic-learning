import random

# variable of python
x = 5
y = 'my name is sajal'
z = 10.555

#!👇 global variable (variable that are created outside of a function are known as global variable)
x = 100
y = 4


def myFunc1():
    x = 200  # this variable is not act as a local variable
    print('value of x inside myFunc1 = ', x)


def myFunc2():
    global y
    y = 500  # this is a global variable
    print('value of y inside myFunc2 = ', y)


print('--- global variable ---')
print('value of x outside myFunc1 = ', x)
myFunc1()
myFunc2()
print('value of y outside myFunc2 = ', y)

#!👇 variable name
myVariableName = "John"  # Camel Case
MyVariableName = "John"  # Pascal Case
my_variable_name = "John"  # Snake case


#!👇 Assign multiple values
x, y, z = 'sajal', 'shati', 'bithi'
print('---- Assign multiple values -----')
print('value of x = ' + x + '\nvalue of y = ' + y + '\nvalue of z = ' + z)


#!👇 Assign one value to multiple variable
x = y = z = 'python developer'
print('---- Assign one value to multiple variable -----')
print('value of x = ' + x + '\nvalue of y = ' + y + '\nvalue of z = ' + z)


#!👇 unpack a collection of data.. it's work like js array destructuring
x, y, z = ['dhaka', 'rajshahi', 'khulna']
print('---- Unpack a collection of data -----')
print('value of x = ' + x + '\nvalue of y = ' + y + '\nvalue of z = ' + z)


#!👇⭐ data type of python ⭐👇
"""
* Text Type:	str
* Numeric Types:	int, float, complex
* Sequence Types:	list, tuple, range
* Mapping Type:	dict
* Set Types:	set, frozenset
* Boolean Type:	bool
* Binary Types:	bytes, bytearray, memoryview
"""

a1 = "Hello World"                              # data type is str
a2 = 20                                         # data type is int
a3 = 20.5                                       # data type is float
a4 = 1j                                         # data type is complex
a5 = ["apple", "banana", "cherry"]              # data type is list
a6 = ("apple", "banana", "cherry")              # data type is tuple
a7 = x = range(6)                               # data type is range
a8 = {"name": "John", "age": 36}                # data type is dist
a9 = {"apple", "banana", "cherry"}              # data type is set
a10 = frozenset({"apple", "banana", "cherry"})  # data type is frozenset
a11 = True                                      # data type is boolean
a12 = b"Hello"                                  # data type is bytes
a13 = bytearray(5)                              # data type is bytearray
a14 = memoryview(bytes(5))                      # data type is memoryview

print('---- data type ----')
print('a1 == ', a1, ' -> ', type(a1))           # check data type
print('a2 == ', a2, ' -> ', type(a2))           # check data type
print('a3 == ', a3, ' -> ', type(a3))           # check data type
print('a4 == ', a4, ' -> ', type(a4))           # check data type
print('a5 == ', a5, ' -> ', type(a5))           # check data type
print('a6 == ', a6, ' -> ', type(a6))           # check data type
print('a7 == ', a7, ' -> ', type(a7))           # check data type
print('a8 == ', a8, ' -> ', type(a8))           # check data type
print('a9 == ', a9, ' -> ', type(a9))           # check data type
print('a10 == ', a10, ' -> ', type(a10))        # check data type
print('a11 == ', a11, ' -> ', type(a11))        # check data type
print('a12 == ', a12, ' -> ', type(a12))        # check data type
print('a13 == ', a13, ' -> ', type(a13))        # check data type
print('a14 == ', a14, ' -> ', type(a14))        # check data type

#!👇 setting specific data type

"""
* x = str("Hello World")	str	
* x = int(20)	int	
* x = float(20.5)	float	
* x = complex(1j)	complex	
* x = list(("apple", "banana", "cherry"))	list	
* x = tuple(("apple", "banana", "cherry"))	tuple	
* x = range(6)	range	
* x = dict(name="John", age=36)	dict	
* x = set(("apple", "banana", "cherry"))	set	
* x = frozenset(("apple", "banana", "cherry"))	frozenset	
* x = bool(5)	bool	
* x = bytes(5)	bytes	
* x = bytearray(5)	bytearray	
* x = memoryview(bytes(5))	memoryview

"""

#!👇 Type conversion/ Type casting
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)
print('a == ', a, ' -> ', type(a))
print('b == ', b, ' -> ', type(b))
print('c == ', c, ' -> ', type(c))


#!👇 Random number (python doesn't have random() function to make a random number but it has a built in function to make random number *import random)
print('random number between 0-9 = ', random.randrange(1, 10))
