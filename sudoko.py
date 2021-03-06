grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
N=9
def issafe(grid,row,col,num):
    for i in range(9):
        if grid[row][i]==num:return False
        if grid[i][col]==num:return False
    m=row-row%3
    n=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[i+m][j +n]==num:return False
    return True
def solve(grid,row,col):
    if(row==N-1 and col==N):return True
    if(col==N):
        row+=1 
        col=0
    if grid[row][col]>0:return solve(grid,row,col+1)
    for i in range(1,N+1):
        if issafe(grid,row,col,i):
            grid[row][col]=i 
            if solve(grid,row,col+1):return True 
        grid[row][col]=0
    return False
if solve(grid,0,0):
    [print(*i) for i in grid]
else:
    print("Solution Not Possible")
'''
output:
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9
'''
