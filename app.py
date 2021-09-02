# python string
str = "Hello, World!"
print(str[1])

#!👇 looping through a string
for x in str:
    print(x)


#!👇 get the length of a string
str = 'i love my country'
print('length of str = ', len(str))


#!👇 check if a certain phrase or character is present in a string
str = 'my name is sajal'
print('sajal' in str)  # return true
print('khan' not in str)  # return true

if 'sajal' in str:
    print('yes text found!')

if 'khan' not in str:
    print('khan not found inside text')


#!👇 Python - Slicing Strings
# get character positino 2 to positino 5
str = 'my name is sajal'
print('show result position 2+1=3 to 7-1=6 -- ', str[2:7])

# Get the characters from the start to position 5 (not included)
str = "Hello, World!"
print('show result position 0 to 5-1 = 4 ', str[:5])

# Get the characters from position 2, and all the way to the end
str = "Hello, World!"
print('show result position 2 to len-1 == ', str[2:])

# Use negative indexes to start the slice from the end of the string
str = 'Hello, World!'
print('show result position len-5 to len-1 == ', str[-5:-1])


#!👇 Python - Modify Strings
# The upper() method returns the string in upper case
str = 'hello, world!'
print('show str in uppercase -- ', str.upper())

# The lower() method returns the string in lower case
str = 'My Name is Sajal'
print('show text in lowercase - ', str.lower())

# The strip() method removes any whitespace from the beginning or the end
str = '                 wow python is awesome         '
print('remove whitespace from text -- ', str.strip())

# The replace() method replaces a string with another string
str = 'my name is sajal'
print('replace name with another text - ', str.replace('sajal', 'sohrab'))

# The split() method splits the string into substrings if it finds instances of the separator
str = 'Hello,   world'
print('split string with, -- ', str.split(','))


#!👇 Python - String Concatenation
# Merge variable a with variable b into variable c
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + ' '+b
print(c)


#!👇 Python - Format - Strings
age = 36
txt = "My name is John, I am ", age
print(txt)

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#!👇 Python - Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""

#! ✋ python string methods
"""
TODO: Link: https://www.w3schools.com/python/python_strings_methods.asp

* capitalize()	Converts the first character to upper case
* casefold()	Converts string into lower case
* center()	Returns a centered string
* count()	Returns the number of times a specified value occurs in a string
* encode()	Returns an encoded version of the string
* endswith()	Returns true if the string ends with the specified value
* expandtabs()	Sets the tab size of the string
* find()	Searches the string for a specified value and returns the position of where it was found
* format()	Formats specified values in a string
* format_map()	Formats specified values in a string
* index()	Searches the string for a specified value and returns the position of where it was found
* isalnum()	Returns True if all characters in the string are alphanumeric
* isalpha()	Returns True if all characters in the string are in the alphabet
* isdecimal()	Returns True if all characters in the string are decimals
* isdigit()	Returns True if all characters in the string are digits
* isidentifier()	Returns True if the string is an identifier
* islower()	Returns True if all characters in the string are lower case
* isnumeric()	Returns True if all characters in the string are numeric
* isprintable()	Returns True if all characters in the string are printable
* isspace()	Returns True if all characters in the string are whitespaces
* istitle()	Returns True if the string follows the rules of a title
* isupper()	Returns True if all characters in the string are upper case
* join()	Joins the elements of an iterable to the end of the string
* ljust()	Returns a left justified version of the string
* lower()	Converts a string into lower case
* lstrip()	Returns a left trim version of the string
* maketrans()	Returns a translation table to be used in translations
* partition()	Returns a tuple where the string is parted into three parts
* replace()	Returns a string where a specified value is replaced with a specified value
* rfind()	Searches the string for a specified value and returns the last position of where it was found
* rindex()	Searches the string for a specified value and returns the last position of where it was found
* rjust()	Returns a right justified version of the string
* rpartition()	Returns a tuple where the string is parted into three parts
* rsplit()	Splits the string at the specified separator, and returns a list
* rstrip()	Returns a right trim version of the string
* split()	Splits the string at the specified separator, and returns a list
* splitlines()	Splits the string at line breaks and returns a list
* startswith()	Returns true if the string starts with the specified value
* strip()	Returns a trimmed version of the string
* swapcase()	Swaps cases, lower case becomes upper case and vice versa
* title()	Converts the first character of each word to upper case
* translate()	Returns a translated string
* upper()	Converts a string into upper case
* zfill()	Fills the string with a specified number of 0 values at the beginning
"""
