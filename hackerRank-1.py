# problem: https://www.hackerrank.com/challenges/python-lists/problem

"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer i at position e
print: Print the list.
remove e: Delete the first occurrence of integer
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of
followed by lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list. 

--------------
Sample Input 
--------------
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

--------------
output
--------------
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
# *👌 --------- solution -------- *👌

mylist = []
n = int(input())

for _ in range(n):
    text, *data = input().split()
    if(text == 'insert'):
        mylist.insert(int(data[0]), int(data[1]))
    if(text == 'append'):
        mylist.append(int(data[0]))
    if(text == 'sort'):
        mylist.sort()
    if(text == 'remove'):
        mylist.remove(int(data[0]))
    if(text == 'pop'):
        mylist.pop()
    if(text == 'reverse'):
        mylist.reverse()
    if(text == 'print'):
        print(mylist)

# *👌 --------- solution -------- *👌
