# python list

"""
TODO: https://www.w3schools.com/python/python_lists.asp
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage
"""

thislist = ["apple", "banana", "cherry"]
print('1-List value = ', thislist)


# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print('2-List constructor = ', thislist)


# * 👇-------------- Python - Access List Items -------------------

# print the second item of the list
thislist = ["apple", "banana", "cherry"]
print('3-second item of a string = ', thislist[1])

#! Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print('4-Last item of the list = ', thislist[-1])

#! Range of Indexes
# it will show data from 2+1=3 to 5-1=4 indexes value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print('5-Range of indexes = ', thislist[2:5])

# it will show value from 0 index to 4-1=3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print('6-range of indexes2 = ', thislist[:4])

# it will show index 2 to len-1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print('7-range of indexes3 = ', thislist[2:])


# it will show index arraylen-4 = 3 to lastindex-1 = 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print('8-range of indexes4 = ', thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# * 👇----------Python - Change List Items---------------
thislist = ["apple", "banana", "cherry"]
thislist[1] = "orange"
print('9-change second item of the list = ', thislist)


# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print('10-change 1,2 index value = ', thislist)

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print('11-change index 1 with two new value = ', thislist)

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print('12-change 1,2 index with another value = ', thislist)


# * 👇-----------Python - Add List Items------------------
#!Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print('13-insert a new item at index 2 = ', thislist)


#! Append Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print('14-add item last index = ', thislist)

#!Extend List
# To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print('15- extend list = ', thislist)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print('15- extend list 2 = ', thislist)


# * 👇------------Python - Remove List Items---------------
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print('16- remove an item from a list = ', thislist)

#! Remove Specified Index
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print('17- remove index 1 from list = ', thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print('18- remove last item = ', thislist)

#! Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print('19- remove first item using del = ', thislist)

#! delete full list
thislist = ["apple", "banana", "cherry"]
del thislist

#! Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print('20- clear the list content = ', thislist)


# * 👇 -------------python - loop list-----------------
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print('loop -- ', x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print('loop index ', i, thislist[i])

# check how many times occur an item inside a list
data = [1, 2, 3, 1, 1, 1, 5, 7]
print('21- 1 occur ', data.count(1), ' times')

# * 👇 -------------- Python - List Comprehension -------------------
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# TODO: https://python.maateen.me/docs/comprehension/
# TODO: https://www.w3schools.com/python/python_lists_comprehension.asp

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print('22- show all fruits which contains a = ', newlist)

# The Syntax
#! newlist = [expression for item in iterable if condition == True]

# * 👇---------------- Python - Sort Lists --------------------------

#!Sort List Asc
thislist = ["zink", "orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print('23- sort list ASC = ', thislist)

#!Sort Descending
thislist = [9, 100, 50, 65, 82, 23, 200]
thislist.sort(reverse=True)
print('24- sort list desc = ', thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function

# Sort the list based on how close the number is to 50:


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print('25- sort list by closer to 50 = ', thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print('26- perform case-insensitive sort = ', thislist)

# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print('27 - reverse order = ', thislist)


# * 👇 ------------- Python - Copy Lists --------------------
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print('28- copy list 1= ', mylist)

# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print('29- copy list 2 =', mylist)

# * 👇 --------------- Python - Join Lists --------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print('30- join list 1 =', list3)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print('31- join list 2 =', list1)


"""
!!!--list methods--!!!
* append()	Adds an element at the end of the list
* clear()	Removes all the elements from the list
* copy()	Returns a copy of the list
* count()	Returns the number of elements with the specified value
* extend()	Add the elements of a list (or any iterable), to the end of the current list
* index()	Returns the index of the first element with the specified value
* insert()	Adds an element at the specified position
* pop()	Removes the element at the specified position
* remove()	Removes the item with the specified value
* reverse()	Reverses the order of the list
* sort()	Sorts the list
!!!--list methods--!!!
"""
