# Problem_11: Largest product in a grid
"""
Q.
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""


#Brute Force

input_matrix = []

for i in range(20):
    line = raw_input().split(" ")
    input_matrix.append(map(int,line))

sup = 0

#Horizontal
for i in range(20):
    for j in range(17):
        temp = input_matrix[i][j] * input_matrix[i][j+1] * input_matrix[i][j+2] *input_matrix[i][j+3]
        if temp > sup:
            sup = temp 
        
#Vertical
for i in range(17):
    for j in range(20):
        temp = input_matrix[i][j] * input_matrix[i+1][j] * input_matrix[i+2][j] *input_matrix[i+3][j]
        if temp > sup:
            sup = temp         

#Diagonal
for i in range(17):
    for j in range(17):
        temp = input_matrix[i][j] * input_matrix[i+1][j+1] * input_matrix[i+2][j+2] *input_matrix[i+3][j+3]
        if temp > sup:
            sup = temp 

for i in range(17):
    for j in range(3,20):
        temp = input_matrix[i][j] * input_matrix[i+1][j-1] * input_matrix[i+2][j-2] *input_matrix[i+3][j-3]
        if temp > sup:
            sup = temp 
