# problem: https://www.hackerrank.com/challenges/list-comprehensions/problem

"""
Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i+j+k) is not equal to n. Here,

input: x,y,z,n

sample input-1:
------------------

1
1
1
2

output:
-----------------
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


"""
# *👌 --------- solution -------- *👌
x, y, z, n = (int(input()) for _ in range(4))

result = [[a, b, c] for a in range(
    0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n]

print(result)

# *👌 --------- solution -------- *👌
