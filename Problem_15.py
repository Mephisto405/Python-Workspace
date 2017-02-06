# Problem_15: Lattice paths
"""
Q.
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
#Typical memoization problem
def latticePaths(n):
    grid = [[0 for i in range(n)] for j in range(n)] #for Memoization
    
    for i in range(n):
        for j in range(n):
            if i == j == 0: #Init
                grid[i][j] = 1
            elif grid[j][i] != 0:
                grid[i][j] = grid[j][i] #Use symmetry for computational efficency
            elif (0 <= i-1) & (0 <= j-1):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
            elif 0 <= i-1:
                grid[i][j] = grid[i-1][j]
            elif 0 <= j-1:
                grid[i][j] = grid[i][j-1]
            else:
                print 'test'
    print2DMatrix(grid,n)
    return grid[n-1][n-1]    

def print2DMatrix(matrix, m):
    for i in range(m):
        print matrix[i]
        print
        
#Or by mathematical intuition, 40!/(20!*20!) = 40Combination20 = answer
