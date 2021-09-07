# problem: https://www.hackerrank.com/challenges/nested-list/problem

"""
Given the names and grades for each student in a class of
students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

sample input:
-------------
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

output:
-----------
Berry
Harry

note:
There are 5 students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. 
The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""
# *👌 --------- solution -------- *👌
n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1] #set e rakhlam unique marks ber korar jonno. r list theke second item nibo

print('\n'.join([name for name, marks in sorted(
    marksheet) if marks == second_highest]))

# *👌 --------- solution -------- *👌
