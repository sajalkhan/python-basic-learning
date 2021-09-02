# variable of python
x = 5
y = 'my name is sajal'
z = 10.555

print('---- data type ----')
print('type of x is == ', type(x))  # check data type
print('type of y is == ', type(y))  # check data type
print('type of z is == ', type(z))  # check data type

#!👇 global variable (variable that are created outside of a function are known as global variable)
x = 100
y = 4


def myFunc1():
    x = 200  # this variable is not act as a local variable
    print('value of x inside myFunc = ', x)


def myFunc2():
    global y
    y = 500  # this is a global variable
    print('value of y inside myFunc2 = ', y)


print('--- global variable ---')
print('value of x outside myFunc = ', x)
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


#!👇 unpack a collection of data.. it's work like js array distructring
x, y, z = ['dhaka', 'rajshahi', 'khulna']
print('---- Unpack a collection of data -----')
print('value of x = ' + x + '\nvalue of y = ' + y + '\nvalue of z = ' + z)
