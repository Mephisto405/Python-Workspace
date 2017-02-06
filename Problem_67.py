# Problem_67: Maximum path sum II
"""
Q.
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""
#Memoization                  *Same algorithm with Problem 18
triangle = []
n = input()
for i in range(n):
    triangle.append(map(int,raw_input().split(' ')))

for i in range(1,n):
    for j in range(n):
        if j <= i:
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max( triangle[i-1][j], triangle[i-1][j-1] )

print reduce( lambda x,y : max(x,y) , triangle[n-1] )
